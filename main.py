import sys
import modules.items
import modules.cart
import signal


def validate_add_item_request():
    item_id = int(input("Masukkan ID dari Item yang diinginkan: "))
    item_quantity = int(input("Masukkan jumlah dari Item yang diinginkan: "))
    return item_id, item_quantity


def exit_app():
    res = input("Apakah Anda yakin ingin keluar dari Aplikasi? y/n ")
    if res == 'y' or res == "Y":
        sys.exit()
    else:
        start_app()


menu_dict = {
    1: modules.items.get_items,
    2: validate_add_item_request,
    0: exit_app
}


def start_app():
    print(
        """
        Selamat Datang di Andy Shop!
        Pilih Menu yang Anda inginkan dengan input nomor menu:
        1. Lihat Semua Produk
        2. Tambahkan Produk ke Keranjang Belanja
        0. Exit
        """
    )
    menu_number = int(input("Masukkan nomor menu: "))

    print(menu_dict[menu_number]())

    start_app()


start_app()