from const import *
from data import *
import time


def print_products(products):
    print('Каталог товаров:\n')
    for i in products:
        print('Название: %s; Цена: %s; Осталось: %s;'
              % (products[i].name, products[i].price, products[i].q_left))
    print('\n')


def add_product(customers, cur_cus, products, orders, cur_ord):
    print_products(products)
    item = input('Введите название товара, который хотите купить\n')
    while item not in products:
        item = input('Введите корректное название товара, который хотите купить\n')
    item_number = input('Введите колличество\n')
    while not item_number.isdigit():
        item_number = input('Введите корректное колличество\n')
    if item not in orders[cur_cus][cur_ord].pos:
        if products[item].check(int(item_number)):
            orders[cur_cus][cur_ord].pos[item] = int(item_number)
        else:
            print('Товара в нужном количестве нет в наличии\n')
    else:
        if products[item].check(item_number + customers[cur_cus].orders[cur_ord][item]):
            orders[cur_cus][cur_ord].pos[item] += int(item_number)
        else:
            print('Товара в нужном количестве нет в наличии\n')


def del_product(customers, cur_cus, products, orders, cur_ord):
    for i in orders[cur_cus][cur_ord].pos:
        print(i)
    item = input('Введите название товара, который хотите удалить\n')
    while item not in orders[cur_cus][cur_ord].pos:
        item = input('Введите корректное название товара, который хотите удалить\n')
    orders[cur_cus][cur_ord].pos.pop(item)


def change_product(customers, cur_cus, products, orders, cur_ord):
    for i in orders[cur_cus][cur_ord].pos:
        print(i)
    item = input('Введите название товара, который хотите изменить\n')
    while item not in orders[cur_cus][cur_ord].pos:
        item = input('Введите корректное название товара, который хотите изменить\n')
    item_number = input('Введите как вы хотите изменить (число с минусом уменьшает)\n')
    while not item_number.isdigit():
        item_number = input('Введите корректно как вы хотите изменить (число с минусом уменьшает)\n')
    if products[item].check(int(item_number) + int(orders[cur_cus][cur_ord].pos[item])):
        orders[cur_cus][cur_ord].pos[item] += int(item_number)
    else:
        print('Товара в нужном количестве нет в наличии\n')


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
              '6 - Просмотр списка своих заказов\n'
              '7 - Просмотр отдельно взятого заказа\n'
              '8 - Редактирование открытого заказа\n'
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
            t = int(time.time())
            orders[cur_cus][str(t)] = Order(str(t), time.ctime(), 'Создан', {}, customers[cur_cus])
            customers[cur_cus].orders.append(str(t))
        elif cur == ADD_ORD:
            for i in customers[cur_cus].orders:
                print('Заказ: ', i)
            cur_ord = input('Введите номер заказа, в который хотите добавить товары\n')
            while cur_ord not in customers[cur_cus].orders:
                cur_ord = input('Введите корректный номер заказа, в который хотите добавить товары\n')
            if orders[cur_cus][cur_ord].status == 'Оплачен':
                print('Заказ уже оплачен!')
                continue
            add_product(customers, cur_cus, products, orders, cur_ord)
        elif cur == MY_ORD:
            for i in orders[cur_cus]:
                print('Заказ: ', i)
                print('Состав:')
                for j in orders[cur_cus][i].pos:
                    print(j, orders[cur_cus][i].pos[j])
                print("Статус: ", orders[cur_cus][i].status)
                print('\n')
        elif cur == CUR_ORD:
            for i in customers[cur_cus].orders:
                print('Заказ: ', i)
            watch_ord = input('Введите номер заказа, который вы хотите просмотреть\n')
            while watch_ord not in customers[cur_cus].orders:
                watch_ord = input('Введите корректный номер заказа, который вы хотите просмотреть\n')
            print('Заказ: ', watch_ord)
            print('Состав:\n')
            for j in orders[cur_cus][watch_ord].pos:
                print(j, orders[cur_cus][watch_ord].pos[j])
            print("Статус: ", orders[cur_cus][i].status)
        elif cur == CHECK:
            for i in customers[cur_cus].orders:
                print('Заказ: ', i)
            watch_ord = input('Введите номер заказа, который вы хотите проверить\n')
            while watch_ord not in customers[cur_cus].orders:
                watch_ord = input('Введите корректный номер заказа, который вы хотите проверить\n')
            if orders[cur_cus][watch_ord].status == 'Оплачен':
                print('Заказ уже оплачен!')
                continue
            if orders[cur_cus][watch_ord].check_all(products):
                print('Все товары в наличии! Оплачено.\n')
                orders[cur_cus][watch_ord].status = 'Оплачен'
                for i in orders[cur_cus][watch_ord].pos:
                    products[i].buy(orders[cur_cus][watch_ord].pos[i], products)
                products = get_products()
            else:
                print('Не все товары в наличии\n')
        elif cur == CH_ORD:
            for i in customers[cur_cus].orders:
                print('Заказ: ', i)
            watch_ord = input('Введите номер заказа, который вы хотите изменить\n')
            while watch_ord not in customers[cur_cus].orders:
                watch_ord = input('Введите корректный номер заказа, который вы хотите изменить\n')
            if orders[cur_cus][watch_ord].status == 'Оплачен':
                print('Заказ уже оплачен!')
                continue
            choice = ['Добавить', 'Удалить', 'Изменить количество']
            print(*choice)
            ans = input('Выберите, что вы хотите сделать\n')
            while ans not in choice:
                ans = input('Выберите из предложенного, что вы хотите сделать\n')
            if ans == choice[0]:
                add_product(customers, cur_cus, products, orders, watch_ord)
            elif ans == choice[1]:
                del_product(customers, cur_cus, products, orders, watch_ord)
            else:
                change_product(customers, cur_cus, products, orders, watch_ord)

