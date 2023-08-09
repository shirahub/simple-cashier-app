import sys

exit_menu = """0. Exit"""


def exit_app():
    res = input("Apakah Anda yakin ingin keluar dari Aplikasi? y/n ")
    if res == 'y' or res == "Y":
        sys.exit()
