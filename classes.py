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


class Order:
    def __init__(self, number: str, date: str, status: str, pos: dict, client: Customer):
        self.number = number
        self.date = date
        self.status = status
        self.pos = pos
        self.client = client

    def check_all(self):
        for i in self.pos:
            if self.pos[i][0] > self.pos[i][1].q_left:
                return False
        return True
