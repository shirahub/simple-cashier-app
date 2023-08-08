import sys
import modules.items
import modules.cart
import signal

cart = {}


def add_item_to_cart():
    item_id, item_quantity = validate_add_item_request()
    global cart
    cart = modules.cart.add_item_to_cart(cart, item_id, item_quantity)
    see_items_in_cart()


def see_items_in_cart():
    total = 0
    for k, v in cart.items():
        product = [x for x in modules.items.get_products() if x.id == k][0]
        total = total + v * product.price
        print("Product: ", product.name, "Quantity: ", v, "Total: ", v * product.price)
    print("Total Seluruhnya: ", total)


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
    "1": modules.items.show_products,
    "2": add_item_to_cart,
    "0": exit_app,
}


def raise_custom_exception(message, exception_type=Exception):
    raise Exception(message)


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
        menu = menu_dict.get(menu_input, lambda: raise_custom_exception("Wrong Menu"))
        menu()
    except Exception as e:
        print(e)

    start_app()


start_app()
