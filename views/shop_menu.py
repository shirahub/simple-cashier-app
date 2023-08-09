import usecases.offering
import usecases.shopping
import views.concern
import utils.errors

menu_dict = {
    "1": usecases.offering.show_products,
    "2": usecases.shopping.add_item_to_cart,
    "3": usecases.shopping.change_item_in_cart,
    "4": usecases.shopping.change_item_qty_in_cart,
    "5": usecases.shopping.remove_item_from_cart,
    "0": views.concern.exit_app,
}

default_menu = """
Selamat Datang di Andy Shop!
Pilih Menu yang Anda inginkan dengan input nomor menu:
1. Lihat Semua Produk
2. Tambahkan Produk ke Keranjang Belanja
"""

conditional_menu = """3. Ganti Produk di Keranjang Belanja
4. Ubah Jumlah Produk di Keranjang Belanja
5. Hapus Produk dari Keranjang Belanja
6.
7.
8. Check Out
"""


def show_shop_menu():
    menu = f"""
    {default_menu + 
     (conditional_menu if not usecases.shopping.cart.is_cart_items_empty() else "") + 
     views.concern.exit_menu}
    """
    print(menu)

    try:
        menu_input = input("Masukkan nomor menu: ")
        if usecases.shopping.cart.is_cart_items_empty() and menu in ["3", "4", "5", "6", "7", "8"]:
            utils.errors.raise_custom_exception("Wrong Menu")
        menu = menu_dict.get(menu_input, lambda: utils.errors.raise_custom_exception("Wrong Menu"))
        menu()
    except Exception as e:
        print(e)

    show_shop_menu()
