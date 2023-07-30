#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import subprocess


def generate_mo_files():
    podir = "po"
    mo = []
    for po in os.listdir(podir):
        if po.endswith(".po"):
            os.makedirs("{}/{}/LC_MESSAGES".format(podir,
                        po.split(".po")[0]), exist_ok=True)
            mo_file = "{}/{}/LC_MESSAGES/{}".format(
                podir, po.split(".po")[0], "Holy_Quran.mo")
            msgfmt_cmd = 'msgfmt {} -o {}'.format(podir + "/" + po, mo_file)
            subprocess.call(msgfmt_cmd, shell=True)
            mo.append(("/usr/share/locale/" + po.split(".po")[0] + "/LC_MESSAGES",
                       ["po/" + po.split(".po")[0] + "/LC_MESSAGES/Holy_Quran.mo"]))
    return mo

print("********************************test")
changelog = "debian/changelog"
if os.path.exists(changelog):
    head = open(changelog).readline()
    try:
        version = head.split("(")[1].split(")")[0]
    except:
        print("debian/changelog format is wrong for get version")
        version = "0.0.0"
    f = open("data/version", "w")
    f.write(version)
    f.close()

data_files = [
    ("/usr/bin", ["Holy_Quran"]),
    ("/usr/share/fonts/", ["KuranKerimFontHamdullah.ttf"]),

    ("/usr/share/applications",
     ["tr.org.bismih.Holy_Quran.desktop"]),

    ("/usr/share/icons",
     ["data/img/Holy_Quran.png"]),

    ("/usr/share/icons/hicolor/scalable/apps/",
     ["data/img/Holy_Quran.png"]),

    ("/usr/share/Holy_Quran/src/",
     ["src/player.py",
      "src/theme.py",
      "src/window.py",
      "src/window_contine.py"]),

    ("/usr/share/Holy_Quran/src/custom_widgets/",
     ["src/Ayat_label.py",
      "src/Btn_ico.py"]),


    ("/usr/share/Holy_Quran/src/db/",
     ["src/db_external_pro.py",
      "src/db_presets.py"]),

    ("/usr/share/Holy_Quran/src/static/",
     ["src/colors.py",
      "src/stc1.py"]),

    ("/usr/share/Holy_Quran/data",
     ["data/Holy_Quran.svg",
      "data/version"]),

    ("/usr/share/Holy_Quran/data",
     ["data/Holy_Quran.svg",
      "data/version"]),

    ("/usr/share/Holy_Quran/",
     ["Kuran.db",
      "LICENSE"]),

] + generate_mo_files()

setup(
    name="Holy_Quran",
    version=version,
    packages=find_packages(),
    scripts=["Holy_Quran"],
    install_requires=["PyGObject", "PySide6==6.5.0", "pygame"],
    data_files=data_files,
    author="Muhammet Halak",
    author_email="halakmuhammet145@gmail.com",
    description="Translate pot file easily",
    license="GPLv3",
    keywords="Holy_Quran , Quran , Holy , Kuran",
    url="https://github.com/halak0013/Kuran-I_Kerim_app",
)
