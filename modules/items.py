class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return "% s name:% s price:% s" % (self.id, self.name, self.price)


products = (
    Product(1, "Kopi", 10_000),
    Product(2, "Susu", 20_000),
    Product(3, "Teh", 30_000)
)


def get_products():
    return products


def show_products():
    for i in products:
        print(i)
