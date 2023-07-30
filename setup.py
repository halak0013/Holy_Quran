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
                podir, po.split(".po")[0], "holy-quran.mo")
            msgfmt_cmd = 'msgfmt {} -o {}'.format(podir + "/" + po, mo_file)
            subprocess.call(msgfmt_cmd, shell=True)
            mo.append(("/usr/share/locale/" + po.split(".po")[0] + "/LC_MESSAGES",
                       ["po/" + po.split(".po")[0] + "/LC_MESSAGES/holy-quran.mo"]))
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
    ("/usr/bin", ["holy-quran"]),
    ("/usr/share/fonts/", ["KuranKerimFontHamdullah.ttf"]),

    ("/usr/share/applications",
     ["tr.org.bismih.holy-quran.desktop"]),

    ("/usr/share/icons",
     ["data/img/holy-quran.png"]),

    ("/usr/share/icons/hicolor/scalable/apps/",
     ["data/img/holy-quran.png"]),

    ("/usr/share/holy-quran/src/",
     ["src/player.py",
      "src/theme.py",
      "src/window.py",
      "src/window_continue.py"]),

    ("/usr/share/holy-quran/src/custom_widgets/",
     ["src/custom_widgets/Ayat_label.py",
      "src/custom_widgets/Btn_ico.py"]),


    ("/usr/share/holy-quran/src/db/",
     ["src/db/db_external_pro.py",
      "src/db/db_presets.py"]),

    ("/usr/share/holy-quran/src/static/",
     ["src/static/colors.py",
      "src/static/stc1.py"]),

    ("/usr/share/holy-quran/data/",
     ["data/version"]),

    ("/usr/share/holy-quran/data/img/",
     ["data/img/holy-quran.png"]),

    ("/usr/share/holy-quran/data/img/icons/",
     ["data/img/icons/search.svg"]),


    ("/usr/share/holy-quran/",
     ["Kuran.db",
      "LICENSE"]),

] + generate_mo_files()

setup(
    name="holy-quran",
    version=version,
    packages=find_packages(),
    scripts=["holy-quran"],
    install_requires=["PyGObject", "PySide6==6.5.0", "pygame"],
    data_files=data_files,
    author="Muhammet Halak",
    author_email="halakmuhammet145@gmail.com",
    description="Translate pot file easily",
    license="GPLv3",
    keywords="holy-quran , Quran , Holy , Kuran",
    url="https://github.com/halak0013/Kuran-I_Kerim_app",
)
