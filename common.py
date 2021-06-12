import sys
from client import *
from owner import *
from data import *
state = 1  # state == 1 client; state == 2 owner

customers = get_customers()
products = get_products()
orders = {}
for i in customers:
    orders[i] = {}
while True:
    print('Кто вы? \n1 - клиент\t 2 - администратор\n'
          '0 - завершить работу')
    n = input('Введите число\n')
    if n == '0':
        sys.exit()
    while n not in ['1', '2']:
        n = input('Введите корректное число\n')
        if n == '0':
            sys.exit()
    state = int(n)
    if state == 1:
        client(customers, products, orders)
    else:
        owner(customers, products, orders)
