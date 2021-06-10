import csv


class Customer:
    def __init__(self, name: str, login: str, password: str, orders: list):
        self.name = name
        self.login = login
        self.password = password
        self.orders = orders


class Products:
    def __init__(self, name: str, price: float, q_left: int):
        self.name = name
        self.price = price
        self.q_left = q_left

    def check(self, n):
        if self.q_left < n:
            return False
        return True

    def buy(self, n, products):
        self.q_left -= int(n)
        with open('products.csv', 'w', encoding="utf8") as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=['price', 'name', 'q_left'])
            writer.writeheader()
            for i in products:
                writer.writerow({'price': products[i].price, 'name': i, 'q_left': str(products[i].q_left)})


class Order:
    def __init__(self, number: str, date: str, status: str, pos: dict, client: Customer):
        self.number = number
        self.date = date
        self.status = status
        self.pos = pos
        self.client = client

    def check_all(self, product):
        for i in self.pos:
            print(self.pos[i])
            if int(self.pos[i]) > product[i].q_left:
                return False
        return True
