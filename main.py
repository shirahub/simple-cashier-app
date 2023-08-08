import modules.items
import modules.cart


def validate_add_item_request():
    item_id = int(input("Masukkan ID dari Item yang diinginkan: "))
    item_quantity = int(input("Masukkan jumlah dari Item yang diinginkan: "))
    return item_id, item_quantity


def start_app():
    usecase_dict = {
        1: modules.items.get_items,
        2: validate_add_item_request
    }

    print(
        """
        Selamat Datang di Andy Shop!
        Pilih Menu yang Anda inginkan dengan input nomor menu:
        1. Lihat Semua Produk
        2. Tambahkan Produk ke Keranjang Belanja
        """
    )
    menu_number = int(input("Masukkan nomor menu: "))

    print(usecase_dict[menu_number]())

    start_app()


start_app()
