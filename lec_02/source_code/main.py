
class Item:
    pay_rate = 0.8  # Скидка 20%
    all_items = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price > 0, f'Price {price} is not > 0'
        assert quantity >= 0, f'Quantity {quantity} is not >= 0'

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all_items.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def print_something(self):
        print('Parent')

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # def __str__(self):
    #     return f'Item: {self.name} {self.price} {self.quantity}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})'


class Lamp(Item):
    def __init__(self, name: str, price: float, quantity=0, lamp_power=40):
        super().__init__(
            name, price, quantity
        )
        assert 0 < lamp_power < 300
        self.lamp_power = lamp_power

    def print_something(self):
        super().print_something()
        print('Child')


def main():
    lamp1 = Lamp('3434', 300, 1)
    print(lamp1.is_integer(4.0))
    # item1 = Item('Jacket', 10000, 1)
    # print(item1.print_something())
    # item1.apply_discount()
    # print(item1.price)
    # print(item1.calculate_total_price())

    # item1.name = 'Jacket'
    # item1.price = 6000
    # print(type(item1.name))
    # item1.quantity = 5

    # item2 = Item('NoteBook', 100000, 1)
    # print(Item.all_items)
    # item2.pay_rate = 0.7
    # item2.apply_discount()
    # print(item2.price)
    # print(item2.calculate_total_price())

    # item2.name = 'NoteBook'
    # item2.price = 50000
    # item2.quantity = 3
    # item1 = 'Jacket'
    # item1_price = 6000
    # item1_quantity = 5
    # item1_price_total = item1_price * item1_quantity


if __name__ == '__main__':
    main()
