import sys
import usecases.offering
import usecases.shopping
import utils.errors


def exit_app():
    res = input("Apakah Anda yakin ingin keluar dari Aplikasi? y/n ")
    if res == 'y' or res == "Y":
        sys.exit()
    else:
        start_app()


menu_dict = {
    "1": usecases.offering.show_products,
    "2": usecases.shopping.add_item_to_cart,
    "0": exit_app,
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

    try:
        menu_input = input("Masukkan nomor menu: ")
        menu = menu_dict.get(menu_input, lambda: utils.errors.raise_custom_exception("Wrong Menu"))
        menu()
    except Exception as e:
        print(e)

    start_app()


start_app()
