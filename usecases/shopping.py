import modules.items
import modules.cart
import utils.inputs

cart = modules.cart.Cart()


def validate_item_id(id):
    product = modules.items.get_product_by_id(id)
    return product


def add_item_to_cart():
    global cart
    item_id = utils.inputs.input_int("Input ID dari Produk: ", "Periksa kembali Input ID Produk Anda.")
    product = validate_item_id(item_id)
    item_qty = utils.inputs.input_int("Input Jumlah dari Produk: ", "Periksa kembali Input Jumlah Produk Anda.")
    cart.add_item_to_cart(item_id, item_qty)
    see_items_in_cart()


def see_items_in_cart():
    global cart
    total = 0

    for k, v in cart.get_items().items():
        product = [x for x in modules.items.get_products() if x.id == k][0]
        total = total + v * product.price
        print("Product: ", product.name, "Quantity: ", v, "Total: ", v * product.price)
    print("Total Seluruhnya: ", total)


def remove_item_from_cart():
    global cart
    item_id = utils.inputs.input_int("Input ID dari Produk yang ingin dihapus: ", "Periksa kembali Input ID Produk Anda.")
    cart.remove_item_from_cart(item_id)
    see_items_in_cart()
