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


class Order:
    def __init__(self, number: int, date: str, status: str, pos: list, client: Customer):
        self.number = number
        self.date = date
        self.status = status
        self.pos = pos
        self.client = client