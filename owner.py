from const import *
from data import *
from client import print_products


def owner(customers, products, orders):
    print('Выберите необходимое действие\n')
    print('1 - Просмотр каталога товаров\n'
          '2 - Изменение текущей цены\n'
          '3 - Изменение количества товаров\n'
          '4 - Просмотр открытых заказов\n'
          '5 - Изменение статуса заказа\n'
          '0 - Выход из системы')
    n = input('Введите число\n')
    if n == '0':
        return
    while not (n.isdigit() and len(n) == 1):
        n = input('Введите корректное число\n')
        if n == '0':
            return
    cur = int(n)
    if cur == CATAL:
        print_products(products)
    elif cur == CH_PRICE:
        print_products(products)
        item = input('Введите название товара, цену которого хотите изменить\n')
        while item not in products:
            item = input('Введите корректное название товара, цену которого хотите изменить\n')
        price = input('Введите новую цену\n')
        while not price.isdigit():
            price = input('Введите корректно новую цену\n')
        products[item].change_price(price, products)
    elif cur == CH_NUMB:
        print_products(products)
        item = input('Введите название товара, который хотите изменить\n')
        while item not in products:
            item = input('Введите корректное название товара, который хотите изменить\n')
        item_number = input('Введите количество товара\n')
        while not item_number.isdigit() or int(item_number) < 0:
            item_number = input('Введите корректно количество товара)\n')
        products[item].change_num(item_number, products)
    elif cur == ORD:
        for i in orders:
            for j in orders[i]:
                if orders[i][j].status == 'Оплачен':
                    print('Заказ:', j)
                    for k in orders[i][j].pos:
                        print(k, orders[i][j].pos[k])
    elif cur == CH_STAT:
        cur_orders = []
        for i in orders:
            for j in orders[i]:
                if orders[i][j].status == 'Оплачен':
                    cur_orders.append(j)
        print(*cur_orders)
        cur_ord = input('Введите номер заказа, который хотите изменить\n')
        while cur_ord not in cur_orders:
            cur_ord = input('Введите корректный номер заказа, который хотите изменить\n')
        choice = ['Отправлен', 'Доставлен']
        print(*choice)
        ans = input('Выберите, что вы хотите сделать\n')
        while ans not in choice:
            ans = input('Выберите из предложенного, что вы хотите сделать\n')
        for i in orders:
            for j in orders[i]:
                if orders[i][j].number == cur_ord:
                    orders[i][j].status = ans
