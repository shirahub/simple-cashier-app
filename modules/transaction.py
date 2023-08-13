class TransactionItem:
    def __init__(self, product_id, transaction_created_at_price, quantity):
        self.transaction_id = None
        self.product_id = product_id
        self.price = transaction_created_at_price
        self.quantity = quantity


class Transaction:

    def __init__(self,
                 discount,
                 created_at,
                 items,
                 ):
        self.final_total = 0
        self.total = 0
        self.discount = discount
        self.created_at = created_at
        self.items = items  # type Class TransactionItem
        self.id = None

    def calculate_total(self):
        self.total = 0
        for i in self.items:
            self.total = self.total + i.price * i.quantity

        self.final_total = self.total * (1 - self.discount)

    def __repr__(self):
        return " Total: %.2f, Discount: %.2f, Final Total: %.2f" % (self.total, self.discount, self.final_total)
