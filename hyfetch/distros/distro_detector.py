# This file is automatically generated. Please do not modify.

from __future__ import annotations

from . import AsciiArt

def detect(name: str) -> AsciiArt | None:
    if not name:
        return None
    name = name.lower()
    if name.startswith('aix'):
        from .aix import aix
        return aix
    
    if name.startswith('aperio gnu/linux'):
        from .aperio_gnu_linux import aperio_gnu_linux
        return aperio_gnu_linux
    
    if name.startswith('aperture'):
        from .aperture import aperture
        return aperture
    
    if name.startswith('asahi'):
        from .asahi import asahi
        return asahi
    
    if name.startswith('hash'):
        from .hash import hash
        return hash
    
    if name.startswith('hardclanz'):
        from .hardclanz import hardclanz
        return hardclanz
    
    if name.startswith('almalinux'):
        from .almalinux import almalinux
        return almalinux
    
    if name.startswith('exodia predator os') or name.startswith('exodia-predator') or name.startswith('predator'):
        from .exodia_predator_os import exodia_predator_os
        return exodia_predator_os
    
    if name == 'alpine_small':
        from .alpine_small import alpine_small
        return alpine_small
    
    if name.startswith('alpine'):
        from .alpine import alpine
        return alpine
    
    if name.startswith('alter'):
        from .alter import alter
        return alter
    
    if name.startswith('amazon'):
        from .amazon import amazon
        return amazon
    
    if name.startswith('amogos'):
        from .amogos import amogos
        return amogos
    
    if name.startswith('anarchy'):
        from .anarchy import anarchy
        return anarchy
    
    if name.startswith('android_small'):
        from .android_small import android_small
        return android_small
    
    if name.startswith('android'):
        from .android import android
        return android
    
    if name.startswith('arselinux'):
        from .arselinux import arselinux
        return arselinux
    
    if name.startswith('instantos'):
        from .instantos import instantos
        return instantos
    
    if name.startswith('antergos'):
        from .antergos import antergos
        return antergos
    
    if name.startswith('antix'):
        from .antix import antix
        return antix
    
    if name.startswith('aosc os/retro'):
        from .aosc_os_retro import aosc_os_retro
        return aosc_os_retro
    
    if name == 'aoscosretro_small':
        from .aoscosretro_small import aoscosretro_small
        return aoscosretro_small
    
    if name.startswith('aosc os'):
        from .aosc_os import aosc_os
        return aosc_os
    
    if name.startswith('apricity'):
        from .apricity import apricity
        return apricity
    
    if name.startswith('archcraft'):
        from .archcraft import archcraft
        return archcraft
    
    if name.startswith('arcolinux_small'):
        from .arcolinux_small import arcolinux_small
        return arcolinux_small
    
    if name.startswith('arcolinux'):
        from .arcolinux import arcolinux
        return arcolinux
    
    if name == 'arch_small':
        from .arch_small import arch_small
        return arch_small
    
    if name == 'arch_old':
        from .arch_old import arch_old
        return arch_old
    
    if name.startswith('archbox'):
        from .archbox import archbox
        return archbox
    
    if name.startswith('archlabs'):
        from .archlabs import archlabs
        return archlabs
    
    if name.startswith('archstrike'):
        from .archstrike import archstrike
        return archstrike
    
    if name.startswith('astos'):
        from .astos import astos
        return astos
    
    if (name.startswith('xferience') or name.endswith('xferience')):
        from .xferience import xferience
        return xferience
    
    if name.startswith('stock linux'):
        from .stock_linux import stock_linux
        return stock_linux
    
    if name.startswith('archmerge'):
        from .archmerge import archmerge
        return archmerge
    
    if name.startswith('arch'):
        from .arch import arch
        return arch
    
    if name.startswith('artix_small'):
        from .artix_small import artix_small
        return artix_small
    
    if name.startswith('artix'):
        from .artix import artix
        return artix
    
    if name.startswith('cobalt'):
        from .cobalt import cobalt
        return cobalt
    
    if name.startswith('arya'):
        from .arya import arya
        return arya
    
    if name.startswith('asteroidos'):
        from .asteroidos import asteroidos
        return asteroidos
    
    if name.startswith('aster'):
        from .aster import aster
        return aster
    
    if name.startswith('bedrock'):
        from .bedrock import bedrock
        return bedrock
    
    if name.startswith('biglinux'):
        from .biglinux import biglinux
        return biglinux
    
    if name.startswith('bitrig'):
        from .bitrig import bitrig
        return bitrig
    
    if name.startswith('blackarch'):
        from .blackarch import blackarch
        return blackarch
    
    if name.startswith('blackpanther') or name.startswith('blackpanther'):
        from .blackpanther import blackpanther
        return blackpanther
    
    if name.startswith('matuusos'):
        from .matuusos import matuusos
        return matuusos
    
    if name.startswith('blag'):
        from .blag import blag
        return blag
    
    if name.startswith('blankon'):
        from .blankon import blankon
        return blankon
    
    if name.startswith('bluelight'):
        from .bluelight import bluelight
        return bluelight
    
    if name.startswith('bodhi'):
        from .bodhi import bodhi
        return bodhi
    
    if name.startswith('bonsai'):
        from .bonsai import bonsai
        return bonsai
    
    if name == 'bsd':
        from .bsd import bsd
        return bsd
    
    if name.startswith('bunsenlabs'):
        from .bunsenlabs import bunsenlabs
        return bunsenlabs
    
    if name.startswith('cachyos'):
        from .cachyos import cachyos
        return cachyos
    
    if name.startswith('calculate'):
        from .calculate import calculate
        return calculate
    
    if name.startswith('carbs'):
        from .carbs import carbs
        return carbs
    
    if name == 'calinixos':
        from .calinixos import calinixos
        return calinixos
    
    if name.startswith('calinixos_small'):
        from .calinixos_small import calinixos_small
        return calinixos_small
    
    if name.startswith('cbl-mariner'):
        from .cbl_mariner import cbl_mariner
        return cbl_mariner
    
    if name.startswith('celos'):
        from .celos import celos
        return celos
    
    if name.startswith('centos_small'):
        from .centos_small import centos_small
        return centos_small
    
    if name.startswith('centos'):
        from .centos import centos
        return centos
    
    if name.startswith('center'):
        from .center import center
        return center
    
    if name.startswith('chakra'):
        from .chakra import chakra
        return chakra
    
    if name.startswith('chaletos'):
        from .chaletos import chaletos
        return chaletos
    
    if name.startswith('chapeau'):
        from .chapeau import chapeau
        return chapeau
    
    if name.startswith('chonkysealos'):
        from .chonkysealos import chonkysealos
        return chonkysealos
    
    if name.startswith('chrom'):
        from .chrom import chrom
        return chrom
    
    if name.startswith('cleanjaro_small'):
        from .cleanjaro_small import cleanjaro_small
        return cleanjaro_small
    
    if name.startswith('cleanjaro'):
        from .cleanjaro import cleanjaro
        return cleanjaro
    
    if name.startswith('clearos'):
        from .clearos import clearos
        return clearos
    
    if name.startswith('clear linux os') or name.startswith('clear_linux'):
        from .clear_linux_os import clear_linux_os
        return clear_linux_os
    
    if name.startswith('clover'):
        from .clover import clover
        return clover
    
    if name.startswith('condres'):
        from .condres import condres
        return condres
    
    if name.startswith('container linux by coreos') or name.startswith('container_linux'):
        from .container_linux_by_coreos import container_linux_by_coreos
        return container_linux_by_coreos
    
    if name == 'crux_small' or name.startswith('kiss'):
        from .crux_small import crux_small
        return crux_small
    
    if name.startswith('crux'):
        from .crux import crux
        return crux
    
    if (name.startswith('crystal linux') or name.endswith('crystal linux')):
        from .crystal_linux import crystal_linux
        return crystal_linux
    
    if (name.startswith('cucumber') or name.endswith('cucumber')):
        from .cucumber import cucumber
        return cucumber
    
    if name.startswith('cutefishos'):
        from .cutefishos import cutefishos
        return cutefishos
    
    if name.startswith('cuteos'):
        from .cuteos import cuteos
        return cuteos
    
    if name.startswith('cyberos'):
        from .cyberos import cyberos
        return cyberos
    
    if name.startswith('dahlia'):
        from .dahlia import dahlia
        return dahlia
    
    if name == 'debian_small':
        from .debian_small import debian_small
        return debian_small
    
    if name.startswith('debian'):
        from .debian import debian
        return debian
    
    if name.startswith('droidian'):
        from .droidian import droidian
        return droidian
    
    if name.startswith('deepin'):
        from .deepin import deepin
        return deepin
    
    if name == 'desaos':
        from .desaos import desaos
        return desaos
    
    if name.startswith('devuan'):
        from .devuan import devuan
        return devuan
    
    if name.startswith('dietpi'):
        from .dietpi import dietpi
        return dietpi
    
    if name.startswith('dracos'):
        from .dracos import dracos
        return dracos
    
    if name == 'darkos':
        from .darkos import darkos
        return darkos
    
    if name.startswith('itc'):
        from .itc import itc
        return itc
    
    if name.startswith('dragonfly_old'):
        from .dragonfly_old import dragonfly_old
        return dragonfly_old
    
    if name.startswith('dragonfly_small'):
        from .dragonfly_small import dragonfly_small
        return dragonfly_small
    
    if name.startswith('dragonfly'):
        from .dragonfly import dragonfly
        return dragonfly
    
    if name.startswith('drauger'):
        from .drauger import drauger
        return drauger
    
    if name.startswith('elementary_small'):
        from .elementary_small import elementary_small
        return elementary_small
    
    if name.startswith('elementary'):
        from .elementary import elementary
        return elementary
    
    if name.startswith('elive'):
        from .elive import elive
        return elive
    
    if name.startswith('endeavouros'):
        from .endeavouros import endeavouros
        return endeavouros
    
    if name.startswith('encryptos'):
        from .encryptos import encryptos
        return encryptos
    
    if name.startswith('endless'):
        from .endless import endless
        return endless
    
    if name.startswith('enso'):
        from .enso import enso
        return enso
    
    if name.startswith('eurolinux'):
        from .eurolinux import eurolinux
        return eurolinux
    
    if name.startswith('exherbo'):
        from .exherbo import exherbo
        return exherbo
    
    if name == 'fedora_small':
        from .fedora_small import fedora_small
        return fedora_small
    
    if name.startswith('fedora_old') or name.startswith('rfremix'):
        from .fedora_old import fedora_old
        return fedora_old
    
    if name.startswith('fedora'):
        from .fedora import fedora
        return fedora
    
    if name.startswith('feren'):
        from .feren import feren
        return feren
    
    if name.startswith('finnix'):
        from .finnix import finnix
        return finnix
    
    if name == 'freebsd_small':
        from .freebsd_small import freebsd_small
        return freebsd_small
    
    if name.startswith('freebsd') or name.startswith('hardenedbsd'):
        from .freebsd import freebsd
        return freebsd
    
    if name.startswith('freemint'):
        from .freemint import freemint
        return freemint
    
    if name.startswith('frugalware'):
        from .frugalware import frugalware
        return frugalware
    
    if name.startswith('funtoo'):
        from .funtoo import funtoo
        return funtoo
    
    if name.startswith('galliumos'):
        from .galliumos import galliumos
        return galliumos
    
    if name == 'garuda_small':
        from .garuda_small import garuda_small
        return garuda_small
    
    if name.startswith('garuda'):
        from .garuda import garuda
        return garuda
    
    if name == 'gentoo_small':
        from .gentoo_small import gentoo_small
        return gentoo_small
    
    if name.startswith('gentoo'):
        from .gentoo import gentoo
        return gentoo
    
    if name.startswith('pentoo'):
        from .pentoo import pentoo
        return pentoo
    
    if name.startswith('glaucus'):
        from .glaucus import glaucus
        return glaucus
    
    if name.startswith('gnewsense'):
        from .gnewsense import gnewsense
        return gnewsense
    
    if name.startswith('gnome'):
        from .gnome import gnome
        return gnome
    
    if name == 'gnu':
        from .gnu import gnu
        return gnu
    
    if name.startswith('gobolinux'):
        from .gobolinux import gobolinux
        return gobolinux
    
    if name.startswith('grapheneos'):
        from .grapheneos import grapheneos
        return grapheneos
    
    if name.startswith('grombyang'):
        from .grombyang import grombyang
        return grombyang
    
    if name.startswith('guix_small'):
        from .guix_small import guix_small
        return guix_small
    
    if name.startswith('guix'):
        from .guix import guix
        return guix
    
    if name.startswith('haiku_small'):
        from .haiku_small import haiku_small
        return haiku_small
    
    if name.startswith('haiku'):
        from .haiku import haiku
        return haiku
    
    if name.startswith('hamonikr'):
        from .hamonikr import hamonikr
        return hamonikr
    
    if name.startswith('huayra'):
        from .huayra import huayra
        return huayra
    
    if name.startswith('hydroos'):
        from .hydroos import hydroos
        return hydroos
    
    if name.startswith('hyperbola_small'):
        from .hyperbola_small import hyperbola_small
        return hyperbola_small
    
    if name.startswith('hyperbola'):
        from .hyperbola import hyperbola
        return hyperbola
    
    if name.startswith('hybrid'):
        from .hybrid import hybrid
        return hybrid
    
    if name.startswith('iglunix') or name.startswith('iglu'):
        from .iglunix import iglunix
        return iglunix
    
    if name.startswith('januslinux') or name.startswith('janus') or name.startswith('ataraxia linux') or name.startswith('ataraxia'):
        from .januslinux import januslinux
        return januslinux
    
    if name.startswith('kaisen'):
        from .kaisen import kaisen
        return kaisen
    
    if name == 'kali_small' or name == 'kalilinux_small' or name == 'kali_linux_small':
        from .kali_small import kali_small
        return kali_small
    
    if name.startswith('kali'):
        from .kali import kali
        return kali
    
    if name.startswith('kaos'):
        from .kaos import kaos
        return kaos
    
    if name.startswith('kde'):
        from .kde import kde
        return kde
    
    if name.startswith('kibojoe'):
        from .kibojoe import kibojoe
        return kibojoe
    
    if name.startswith('kogaion'):
        from .kogaion import kogaion
        return kogaion
    
    if name.startswith('korora'):
        from .korora import korora
        return korora
    
    if name.startswith('kslinux'):
        from .kslinux import kslinux
        return kslinux
    
    if name.startswith('kubuntu'):
        from .kubuntu import kubuntu
        return kubuntu
    
    if name.startswith('lede'):
        from .lede import lede
        return lede
    
    if name == 'langitketujuh_old':
        from .langitketujuh_old import langitketujuh_old
        return langitketujuh_old
    
    if name.startswith('langitketujuh'):
        from .langitketujuh import langitketujuh
        return langitketujuh
    
    if name.startswith('laxeros'):
        from .laxeros import laxeros
        return laxeros
    
    if name.startswith('libreelec'):
        from .libreelec import libreelec
        return libreelec
    
    if name == 'linux':
        from .linux import linux
        return linux
    
    if name.startswith('linuxlite_small'):
        from .linuxlite_small import linuxlite_small
        return linuxlite_small
    
    if name.startswith('linux lite') or name.startswith('linux_lite'):
        from .linux_lite import linux_lite
        return linux_lite
    
    if name.startswith('lmde'):
        from .lmde import lmde
        return lmde
    
    if name.startswith('lubuntu'):
        from .lubuntu import lubuntu
        return lubuntu
    
    if name.startswith('lunar'):
        from .lunar import lunar
        return lunar
    
    if name == 'mac"*"_small':
        from .mac_small import mac_small
        return mac_small
    
    if name.startswith('mac') or name == 'darwin':
        from .mac import mac
        return mac
    
    if name.startswith('mageia_small'):
        from .mageia_small import mageia_small
        return mageia_small
    
    if name.startswith('mageia'):
        from .mageia import mageia
        return mageia
    
    if name.startswith('magpieos'):
        from .magpieos import magpieos
        return magpieos
    
    if name.startswith('mandriva') or name.startswith('mandrake'):
        from .mandriva import mandriva
        return mandriva
    
    if name.startswith('manjaro_small'):
        from .manjaro_small import manjaro_small
        return manjaro_small
    
    if name.startswith('manjaro'):
        from .manjaro import manjaro
        return manjaro
    
    if name.startswith('massos'):
        from .massos import massos
        return massos
    
    if name.startswith('tearch'):
        from .tearch import tearch
        return tearch
    
    if name.startswith('maui'):
        from .maui import maui
        return maui
    
    if name.startswith('mer'):
        from .mer import mer
        return mer
    
    if name.startswith('minix'):
        from .minix import minix
        return minix
    
    if name.startswith('miracle linux') or name.startswith('miracle_linux'):
        from .miracle_linux import miracle_linux
        return miracle_linux
    
    if name.startswith('linspire') or name.startswith('freespire') or name.startswith('lindows'):
        from .linspire import linspire
        return linspire
    
    if name.startswith('linuxmint_small'):
        from .linuxmint_small import linuxmint_small
        return linuxmint_small
    
    if name.startswith('linux mint old') or name.startswith('linuxmintold') or name.startswith('mint_old'):
        from .linux_mint_old import linux_mint_old
        return linux_mint_old
    
    if name.startswith('linux mint') or name.startswith('linuxmint') or name.startswith('mint'):
        from .linux_mint import linux_mint
        return linux_mint
    
    if name.startswith('live raizo') or name.startswith('live_raizo'):
        from .live_raizo import live_raizo
        return live_raizo
    
    if name.startswith('mx_small'):
        from .mx_small import mx_small
        return mx_small
    
    if name.startswith('mx'):
        from .mx import mx
        return mx
    
    if name.startswith('namib'):
        from .namib import namib
        return namib
    
    if name.startswith('nekos'):
        from .nekos import nekos
        return nekos
    
    if name.startswith('neptune'):
        from .neptune import neptune
        return neptune
    
    if name.startswith('netbsd_small'):
        from .netbsd_small import netbsd_small
        return netbsd_small
    
    if name.startswith('netbsd'):
        from .netbsd import netbsd
        return netbsd
    
    if name.startswith('netrunner'):
        from .netrunner import netrunner
        return netrunner
    
    if name.startswith('nitrux'):
        from .nitrux import nitrux
        return nitrux
    
    if name == 'nixos_small':
        from .nixos_small import nixos_small
        return nixos_small
    
    if name.startswith('nixos_old'):
        from .nixos_old import nixos_old
        return nixos_old
    
    if name.startswith('nixos'):
        from .nixos import nixos
        return nixos
    
    if name.startswith('nomadbsd'):
        from .nomadbsd import nomadbsd
        return nomadbsd
    
    if name.startswith('ghostbsd'):
        from .ghostbsd import ghostbsd
        return ghostbsd
    
    if name.startswith('nurunner'):
        from .nurunner import nurunner
        return nurunner
    
    if name.startswith('nutyx'):
        from .nutyx import nutyx
        return nutyx
    
    if name.startswith('obrevenge'):
        from .obrevenge import obrevenge
        return obrevenge
    
    if name.startswith('omnios'):
        from .omnios import omnios
        return omnios
    
    if name == 'openbsd_small':
        from .openbsd_small import openbsd_small
        return openbsd_small
    
    if name.startswith('openbsd'):
        from .openbsd import openbsd
        return openbsd
    
    if name.startswith('openeuler'):
        from .openeuler import openeuler
        return openeuler
    
    if name.startswith('openindiana'):
        from .openindiana import openindiana
        return openindiana
    
    if name.startswith('openmamba'):
        from .openmamba import openmamba
        return openmamba
    
    if name.startswith('openmandriva'):
        from .openmandriva import openmandriva
        return openmandriva
    
    if name.startswith('openstage'):
        from .openstage import openstage
        return openstage
    
    if name.startswith('openwrt'):
        from .openwrt import openwrt
        return openwrt
    
    if name.startswith('open source media center') or name == 'osmc':
        from .open_source_media_center import open_source_media_center
        return open_source_media_center
    
    if name.startswith('opnsense'):
        from .opnsense import opnsense
        return opnsense
    
    if name.startswith('oracle'):
        from .oracle import oracle
        return oracle
    
    if name.startswith('orchid_small'):
        from .orchid_small import orchid_small
        return orchid_small
    
    if name.startswith('orchid'):
        from .orchid import orchid
        return orchid
    
    if name.startswith('os elbrus'):
        from .os_elbrus import os_elbrus
        return os_elbrus
    
    if name.startswith('pacbsd'):
        from .pacbsd import pacbsd
        return pacbsd
    
    if name.startswith('parabola_small'):
        from .parabola_small import parabola_small
        return parabola_small
    
    if name.startswith('parabola'):
        from .parabola import parabola
        return parabola
    
    if name.startswith('pardus'):
        from .pardus import pardus
        return pardus
    
    if name.startswith('parrot'):
        from .parrot import parrot
        return parrot
    
    if name.startswith('parsix'):
        from .parsix import parsix
        return parsix
    
    if name.startswith('pcbsd') or name.startswith('trueos'):
        from .pcbsd import pcbsd
        return pcbsd
    
    if name.startswith('pclinuxos'):
        from .pclinuxos import pclinuxos
        return pclinuxos
    
    if name.startswith('pearos'):
        from .pearos import pearos
        return pearos
    
    if name.startswith('pengwin'):
        from .pengwin import pengwin
        return pengwin
    
    if name.startswith('peppermint'):
        from .peppermint import peppermint
        return peppermint
    
    if name.startswith('pisi'):
        from .pisi import pisi
        return pisi
    
    if name.startswith('pnm linux') or name.startswith('whpnm linux'):
        from .pnm_linux import pnm_linux
        return pnm_linux
    
    if name.startswith('popos_small') or name.startswith('pop_os_small'):
        from .popos_small import popos_small
        return popos_small
    
    if name.startswith('pop!_os') or name.startswith('popos') or name.startswith('pop_os'):
        from .pop__os import pop__os
        return pop__os
    
    if name.startswith('porteus'):
        from .porteus import porteus
        return porteus
    
    if name == 'postmarketos_small':
        from .postmarketos_small import postmarketos_small
        return postmarketos_small
    
    if name.startswith('postmarketos'):
        from .postmarketos import postmarketos
        return postmarketos
    
    if name.startswith('puffos'):
        from .puffos import puffos
        return puffos
    
    if name.startswith('proxmox'):
        from .proxmox import proxmox
        return proxmox
    
    if name.startswith('puppy') or name.startswith('quirky werewolf') or name.startswith('precise puppy'):
        from .puppy import puppy
        return puppy
    
    if name.startswith('pureos_small'):
        from .pureos_small import pureos_small
        return pureos_small
    
    if name.startswith('pureos'):
        from .pureos import pureos
        return pureos
    
    if name.startswith('q4os'):
        from .q4os import q4os
        return q4os
    
    if name.startswith('qubes'):
        from .qubes import qubes
        return qubes
    
    if name.startswith('qubyt'):
        from .qubyt import qubyt
        return qubyt
    
    if name.startswith('quibian'):
        from .quibian import quibian
        return quibian
    
    if name.startswith('radix'):
        from .radix import radix
        return radix
    
    if name.startswith('raspbian_small'):
        from .raspbian_small import raspbian_small
        return raspbian_small
    
    if name.startswith('raspbian'):
        from .raspbian import raspbian
        return raspbian
    
    if name == 'ravynos':
        from .ravynos import ravynos
        return ravynos
    
    if name.startswith('reborn os') or name.startswith('reborn'):
        from .reborn_os import reborn_os
        return reborn_os
    
    if name.startswith('red star') or name.startswith('redstar'):
        from .red_star import red_star
        return red_star
    
    if name.startswith('redcore'):
        from .redcore import redcore
        return redcore
    
    if name == 'redhat_old' or name.startswith('rhel_old'):
        from .redhat_old import redhat_old
        return redhat_old
    
    if name.startswith('redhat') or name.startswith('red hat') or name.startswith('rhel'):
        from .redhat import redhat
        return redhat
    
    if name.startswith('refracted devuan') or name.startswith('refracted_devuan'):
        from .refracted_devuan import refracted_devuan
        return refracted_devuan
    
    if name.startswith('regata'):
        from .regata import regata
        return regata
    
    if name.startswith('regolith'):
        from .regolith import regolith
        return regolith
    
    if name.startswith('rhaymos'):
        from .rhaymos import rhaymos
        return rhaymos
    
    if name.startswith('rocky_small'):
        from .rocky_small import rocky_small
        return rocky_small
    
    if name.startswith('rocky'):
        from .rocky import rocky
        return rocky
    
    if name.startswith('rosa'):
        from .rosa import rosa
        return rosa
    
    if name.startswith('sabotage'):
        from .sabotage import sabotage
        return sabotage
    
    if name.startswith('sabayon'):
        from .sabayon import sabayon
        return sabayon
    
    if name.startswith('sailfish'):
        from .sailfish import sailfish
        return sailfish
    
    if name.startswith('salentos'):
        from .salentos import salentos
        return salentos
    
    if name.startswith('shastraos'):
        from .shastraos import shastraos
        return shastraos
    
    if name.startswith('sasanqua'):
        from .sasanqua import sasanqua
        return sasanqua
    
    if name.startswith('scientific'):
        from .scientific import scientific
        return scientific
    
    if name.startswith('septor'):
        from .septor import septor
        return septor
    
    if name.startswith('serene'):
        from .serene import serene
        return serene
    
    if name.startswith('sharklinux'):
        from .sharklinux import sharklinux
        return sharklinux
    
    if name.startswith('siduction'):
        from .siduction import siduction
        return siduction
    
    if name.startswith('slackware_small'):
        from .slackware_small import slackware_small
        return slackware_small
    
    if name.startswith('slackware'):
        from .slackware import slackware
        return slackware
    
    if name.startswith('slitaz'):
        from .slitaz import slitaz
        return slitaz
    
    if name.startswith('smartos'):
        from .smartos import smartos
        return smartos
    
    if name.startswith('skiffos'):
        from .skiffos import skiffos
        return skiffos
    
    if name.startswith('solus'):
        from .solus import solus
        return solus
    
    if name.startswith('sulin'):
        from .sulin import sulin
        return sulin
    
    if name.startswith('source mage') or name.startswith('source_mage'):
        from .source_mage import source_mage
        return source_mage
    
    if name.startswith('sparky'):
        from .sparky import sparky
        return sparky
    
    if name.startswith('star'):
        from .star import star
        return star
    
    if name.startswith('steamos'):
        from .steamos import steamos
        return steamos
    
    if name == 'sunos_small' or name == 'solaris_small':
        from .sunos_small import sunos_small
        return sunos_small
    
    if name == 'sunos' or name == 'solaris':
        from .sunos import sunos
        return sunos
    
    if name.startswith('opensuse leap') or name.startswith('opensuse_leap'):
        from .opensuse_leap import opensuse_leap
        return opensuse_leap
    
    if name.startswith('t2'):
        from .t2 import t2
        return t2
    
    if name.startswith('opensuse tumbleweed') or name.startswith('opensuse_tumbleweed'):
        from .opensuse_tumbleweed import opensuse_tumbleweed
        return opensuse_tumbleweed
    
    if name == 'opensuse_small' or name.startswith('suse_small'):
        from .opensuse_small import opensuse_small
        return opensuse_small
    
    if name.startswith('opensuse') or name.startswith('open suse') or name.startswith('suse'):
        from .opensuse import opensuse
        return opensuse
    
    if name.startswith('parch') or name.startswith('parch') or name.startswith('parch'):
        from .parch import parch
        return parch
    
    if name.startswith('swagarch'):
        from .swagarch import swagarch
        return swagarch
    
    if name.startswith('tails'):
        from .tails import tails
        return tails
    
    if name.startswith('torizoncore'):
        from .torizoncore import torizoncore
        return torizoncore
    
    if name.startswith('trisquel'):
        from .trisquel import trisquel
        return trisquel
    
    if name.startswith('twister'):
        from .twister import twister
        return twister
    
    if name.startswith('ubuntu cinnamon') or name.startswith('ubuntu-cinnamon'):
        from .ubuntu_cinnamon import ubuntu_cinnamon
        return ubuntu_cinnamon
    
    if name.startswith('ubuntu budgie') or name.startswith('ubuntu-budgie'):
        from .ubuntu_budgie import ubuntu_budgie
        return ubuntu_budgie
    
    if name.startswith('ubuntu-gnome'):
        from .ubuntu_gnome import ubuntu_gnome
        return ubuntu_gnome
    
    if name.startswith('ubuntu kylin') or name.startswith('ubuntu-kylin'):
        from .ubuntu_kylin import ubuntu_kylin
        return ubuntu_kylin
    
    if name.startswith('ubuntu touch'):
        from .ubuntu_touch import ubuntu_touch
        return ubuntu_touch
    
    if name.startswith('ubuntu mate') or name.startswith('ubuntu-mate'):
        from .ubuntu_mate import ubuntu_mate
        return ubuntu_mate
    
    if name == 'ubuntu_old02':
        from .ubuntu_old02 import ubuntu_old02
        return ubuntu_old02
    
    if name.startswith('ubuntu studio') or name == 'ubuntu-studio':
        from .ubuntu_studio import ubuntu_studio
        return ubuntu_studio
    
    if name.startswith('ubuntu sway') or name == 'ubuntu-sway':
        from .ubuntu_sway import ubuntu_sway
        return ubuntu_sway
    
    if name == 'ubuntu_small':
        from .ubuntu_small import ubuntu_small
        return ubuntu_small
    
    if name.startswith('ubuntu_old') or name.startswith('i3buntu'):
        from .ubuntu_old import ubuntu_old
        return ubuntu_old
    
    if name.startswith('floflis'):
        from .floflis import floflis
        return floflis
    
    if name.startswith('ubuntu'):
        from .ubuntu import ubuntu
        return ubuntu
    
    if name.startswith('ultramarine linux') or name.startswith('ultramarine'):
        from .ultramarine_linux import ultramarine_linux
        return ultramarine_linux
    
    if name.startswith('univalent'):
        from .univalent import univalent
        return univalent
    
    if name.startswith('uos'):
        from .uos import uos
        return uos
    
    if name.startswith('univention'):
        from .univention import univention
        return univention
    
    if name.startswith('uwuntu'):
        from .uwuntu import uwuntu
        return uwuntu
    
    if name.startswith('urukos'):
        from .urukos import urukos
        return urukos
    
    if name.startswith('venom'):
        from .venom import venom
        return venom
    
    if name == 'void_small':
        from .void_small import void_small
        return void_small
    
    if name.startswith('void'):
        from .void import void
        return void
    
    if name.startswith('vnux'):
        from .vnux import vnux
        return vnux
    
    if name.startswith('vzlinux'):
        from .vzlinux import vzlinux
        return vzlinux
    
    if name.startswith('yiffos'):
        from .yiffos import yiffos
        return yiffos
    
    if name.startswith('semc'):
        from .semc import semc
        return semc
    
    if name.startswith('vanilla'):
        from .vanilla import vanilla
        return vanilla
    
    if name.startswith('obarun'):
        from .obarun import obarun
        return obarun
    
    if (name.startswith('wii-linux-ngx') or name.endswith('wii-linux-ngx')) or (name.startswith('whiite-linux') or name.endswith('whiite-linux')) or (name.startswith('gc-linux') or name.endswith('gc-linux')):
        from .wii_linux_ngx import wii_linux_ngx
        return wii_linux_ngx
    
    if (name.startswith('[windows 11]') or name.endswith('[windows 11]')) or (name.startswith('on windows 11') or name.endswith('on windows 11')) or name.startswith('windows 11') or name == 'windows11':
        from .windows_11 import windows_11
        return windows_11
    
    if (name.startswith('[windows 10]') or name.endswith('[windows 10]')) or (name.startswith('on windows 10') or name.endswith('on windows 10')) or name.startswith('windows 8') or name.startswith('windows 10') or name == 'windows10' or name == 'windows8':
        from .windows_10 import windows_10
        return windows_10
    
    if name.startswith('windows'):
        from .windows import windows
        return windows
    
    if name.startswith('xubuntu'):
        from .xubuntu import xubuntu
        return xubuntu
    
    if name.startswith('soda'):
        from .soda import soda
        return soda
    
    if name.startswith('krassos') or name.startswith('krass'):
        from .krassos import krassos
        return krassos
    
    if name.startswith('irix'):
        from .irix import irix
        return irix
    
    if name.startswith('zorin'):
        from .zorin import zorin
        return zorin
    
    if name.endswith('bsd'):
        from .bsd import bsd
        return bsd
    
    if name == 'darwin':
        from .darwin import darwin
        return darwin
    
    if name.startswith('gnu'):
        from .gnu import gnu
        return gnu
    
    if name == 'linux':
        from .linux import linux
        return linux
    
    if name.startswith('profelis sambabox') or name.startswith('sambabox'):
        from .profelis_sambabox import profelis_sambabox
        return profelis_sambabox
    
    if name == 'sunos':
        from .sunos import sunos
        return sunos
    