try: 
    class Computer:
        def __init__(self):
            self.__max_price = 900
        def sell(self):
            print("Selling price = {}".format(self.__max_price))
        def set_max_price(self, price):
            self.__max_price = price
    buyer = Computer()
    buyer.__max_price = 1000
    buyer.sell()
    buyer.set_max_price(1000)
    buyer.sell()  
    class Point:
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y
        def __str__(self):
            return "({0}, {1})".format(self.x, self.y)
    p1 = Point(2, 3)
    print(p1)
    class school:
        __schoolname = "MIS"
        def __init__(self, name):
            self.__name = name
        def display(self):
            print("This file is privated")
        def privmeth(self):
            print("Method private")
    obj = school("MIS")
    print(obj.__name)
    obj.privmeth()
    obj.__name
except AttributeError:
    print("File private")