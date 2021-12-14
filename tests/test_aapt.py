from aapt2 import aapt


def test_version():
    print(aapt.version())


def test_pkg_info():
    print(aapt.get_apk_info("$HOME/Downloads/zzt.apk"))


def test_pkg_info():
    print(aapt.ls("$HOME/Downloads/zzt.apk"))
