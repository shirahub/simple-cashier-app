class Cart:
    def __init__(self, items=None):
        if items is None:
            self.items = {}
        else:
            self.items = items

    def add_item_to_cart(self, item_id, item_quantity):
        prev_qty = self.items.get(item_id, 0)
        self.items[item_id] = prev_qty + item_quantity

    def get_items(self):
        return self.items
