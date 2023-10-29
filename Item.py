class Item():
    def __init__(self, item_id, name, price, count):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.count = count

    def get_item_info(self):
        return self.item_id, self.name, f'£{self.price:.2f}', self.count

    def add_n(self, n):
        self.count += n

    def remove_n(self, n):
        if self.count >= n:
            self.count -= n
            return True
        else:
            self.count = 0
            return False