class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def detail(self):
        print(f"name = {self.name}")
        print(f"id = {self.id}")
        print(f"salary = {self.salary}")


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self):
        self.price = self.price * 0.1


class Shooping_cart:
    products = [
        {
            'id' : 1,
            'name': "Pen",
            'price' : 10
        },
        {
            'id' : 2,
            'name': "file paper",
            'price' : 20
        },
    ]

    def __init___(self):
        self.items = []

    def add_item(self,index):
        for item in self.products:
            if item['id'] == index:
                self.items.append(item)
                break

    def remove_item(self,index):
        for i,item in enumerate(self.items):
            if item['id'] == index :
                self.items.remove(i)

    def get_total(self):
        return sum([item['price'] for item in self.items])