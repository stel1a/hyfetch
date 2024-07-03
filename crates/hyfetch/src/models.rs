use serde::{Deserialize, Serialize};

use crate::color_util::Lightness;
use crate::neofetch_util::ColorAlignment;
use crate::presets::Preset;
use crate::types::{AnsiMode, Backend, LightDark};

#[derive(Clone, Debug, Deserialize, Serialize)]
pub struct Config {
    pub preset: Preset,
    pub mode: AnsiMode,
    pub light_dark: LightDark,
    lightness: Option<Lightness>,
    pub color_align: ColorAlignment,
    pub backend: Backend,
    #[serde(default)]
    #[serde(with = "self::args_serde_with")]
    pub args: Option<Vec<String>>,
    pub distro: Option<String>,
    pub pride_month_disable: bool,
}

impl Config {
    pub fn default_lightness(term: &LightDark) -> Lightness {
        match term {
            LightDark::Dark => Lightness::new(0.65).unwrap(),
            LightDark::Light => Lightness::new(0.4).unwrap(),
        }
    }

    pub fn lightness(&self) -> Lightness {
        self.lightness
            .unwrap_or_else(|| Self::default_lightness(&self.light_dark))
    }
}

mod args_serde_with {
    use std::fmt;

    use serde::de::{self, value, Deserialize, Deserializer, SeqAccess, Visitor};
    use serde::ser::Serializer;

    pub(super) fn serialize<S>(
        value: &Option<Vec<String>>,
        serializer: S,
    ) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        match value {
            Some(value) => serializer.serialize_some(&shell_words::join(value)),
            None => serializer.serialize_none(),
        }
    }

    pub(super) fn deserialize<'de, D>(deserializer: D) -> Result<Option<Vec<String>>, D::Error>
    where
        D: Deserializer<'de>,
    {
        struct StringOrVec;

        struct OptionVisitor;

        impl<'de> Visitor<'de> for StringOrVec {
            type Value = Vec<String>;

            fn expecting(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
                formatter.write_str("string or list of strings")
            }

            fn visit_str<E>(self, s: &str) -> Result<Self::Value, E>
            where
                E: de::Error,
            {
                shell_words::split(s).map_err(de::Error::custom)
            }

            fn visit_seq<S>(self, seq: S) -> Result<Self::Value, S::Error>
            where
                S: SeqAccess<'de>,
            {
                Deserialize::deserialize(value::SeqAccessDeserializer::new(seq))
            }
        }

        impl<'de> Visitor<'de> for OptionVisitor {
            type Value = Option<Vec<String>>;

            fn expecting(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
                formatter.write_str("option")
            }

            #[inline]
            fn visit_unit<E>(self) -> Result<Self::Value, E>
            where
                E: de::Error,
            {
                Ok(None)
            }

            #[inline]
            fn visit_none<E>(self) -> Result<Self::Value, E>
            where
                E: de::Error,
            {
                Ok(None)
            }

            #[inline]
            fn visit_some<D>(self, deserializer: D) -> Result<Self::Value, D::Error>
            where
                D: Deserializer<'de>,
            {
                deserializer.deserialize_any(StringOrVec).map(Some)
            }
        }

        deserializer.deserialize_option(OptionVisitor)
    }
}
