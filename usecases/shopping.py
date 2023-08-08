import modules.items
import modules.cart
import utils.inputs

cart = {}

def validate_item_id(id):
    product = modules.items.get_product_by_id(id)
    return product

def add_item_to_cart():
    global cart
    item_id = utils.inputs.input_int("Input ID dari Produk: ", "Periksa kembali Input ID Produk Anda.")
    product = validate_item_id(item_id)
    item_qty = utils.inputs.input_int("Input Jumlah dari Produk: ", "Periksa kembali Input Jumlah Produk Anda.")
    cart = modules.cart.add_item_to_cart(cart, item_id, item_qty)
    see_items_in_cart()


def see_items_in_cart():
    total = 0

    for k, v in cart.items():
        product = [x for x in modules.items.get_products() if x.id == k][0]
        total = total + v * product.price
        print("Product: ", product.name, "Quantity: ", v, "Total: ", v * product.price)
    print("Total Seluruhnya: ", total)