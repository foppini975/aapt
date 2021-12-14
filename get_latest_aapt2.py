#!/usr/bin/env python3
import requests
import shutil
import os
import zipfile

"""
打开 https://maven.google.com/web/index.html?q=aapt#com.android.tools.build:aapt2 
获取最新版本的 aapt2
"""
# AAPT_VERSION = "7.0.4-7396180"
AAPT_VERSION = "7.2.0-alpha05-7832930"
PLATFORMS = [("linux", "Linux"), ("osx", "Darwin"), ("windows", "Windows")]
DOWNLOAD_DIR = "downloads"
LIB_NAME = "aapt2"
TARGET = f"src/{LIB_NAME}/bin"


def download_jars():
    shutil.rmtree(DOWNLOAD_DIR, ignore_errors=True)
    os.makedirs(DOWNLOAD_DIR)
    shutil.rmtree(TARGET, ignore_errors=True)
    os.makedirs(TARGET)
    for platform, system in PLATFORMS:
        url = jar_url(platform=platform, version=AAPT_VERSION)
        file_name = os.path.join(
            DOWNLOAD_DIR, f"{platform}-{AAPT_VERSION}.jar")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        unzip_jar(file_name, system)
    shutil.rmtree(DOWNLOAD_DIR, ignore_errors=True)


def jar_url(platform, version):
    return f"https://dl.google.com/android/maven2/com/android/tools/build/aapt2/{version}/aapt2-{version}-{platform}.jar"


def unzip_jar(file, system):
    zip = zipfile.ZipFile(file, "r")
    file_name = LIB_NAME
    if system == "Windows":
        file_name += '.exe'
    zip.extract(file_name, f"{TARGET}/{system}")


if __name__ == "__main__":
    download_jars()
