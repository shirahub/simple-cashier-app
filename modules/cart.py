class Cart:
    def __init__(self, items=None):
        if items is None:
            self.items = {}
        else:
            self.items = items

    def is_item_exist_in_cart(self, item_id):
        if item_id in self.items:
            return True

        return False

    def add_item_to_cart(self, item_id, item_quantity):
        prev_qty = self.items.get(item_id, 0)
        self.items[item_id] = prev_qty + item_quantity

    def get_items(self):
        return self.items

    def is_cart_items_empty(self):
        if len(self.items) == 0:
            return True

        return False

    def remove_item_from_cart(self, item_id):
        self.items.pop(item_id)

    def change_item_in_cart(self, prev_item_id, new_item_id):
        self.items[new_item_id] = self.items.pop(prev_item_id)

    def change_item_qty_in_cart(self, item_id, item_qty):
        self.items[item_id] = item_qty

