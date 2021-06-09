from const import *
from data import *
import time


def client(customers, products, orders):
    mode = 0  # 0 - не авторизован; 1 - авторизован
    cur_cus = ''
    while True:
        print('Выберите необходимое действие\n')
        print('1 - Просмотр каталога товаров\n'
              '2 - Авторизация в системе по логину и паролю\n'
              '3 - Создание заказа\n'
              '4 - Добавление товаров в заказ\n'
              '5 - Подтверждение заказа\n'
              '6 - Оплата заказа\n'
              '7 - Просмотр списка своих заказов\n'
              '8 - Просмотр отдельно взятого заказа\n'
              '9 - Редактирование открытого заказа\n'
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
            print('Каталог товаров:\n')
            for i in products:
                print('Название: %s; Цена: %s; Осталось: %s;'
                      % (products[i].name, products[i].price, products[i].q_left))
            print('\n')
        elif cur == AUTH:
            if mode == 0:
                log = input('Введите ваш логин\n')
                while log not in customers:
                    log = input('Введите корректный логин\n')
                cur_cus = log
                password = input('Введите ваш пароль\n')
                while customers[cur_cus].password != password:
                    password = input('Введите корректный пароль\n')
                mode = 1
            else:
                print('Вы уже авторизованы\n')
        elif mode == 0:
            print('Сначала авторизуйтесь\n')
        elif cur == MAKE_ORD:
            t = time.time()
            orders[cur_cus].append(Order(int(t), time.ctime(), 'Создан', [], customers[cur_cus]))
            customers[cur_cus].orders.append(int(t))
        elif cur == ADD_ORD:
            for i in customers[cur_cus].orders:
                print('Заказ: ', i)
