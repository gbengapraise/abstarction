class Computer:

    _max_price = 900


    def get_max_price(self):
        return self._max_price
    

    def set_max_price(self, price):
        self._max_price = price

comp = Computer()
print(comp.get_max_price())

comp.set_max_price(1000)
print(comp.get_max_price())