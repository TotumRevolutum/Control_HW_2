import csv
from classes import *


def get_customers():
    customers = {}
    with open('customers.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for i in reader:
            customers[i['login']] = Customer(i['name'], i['login'], i['password'], [])
    return customers


def get_products():
    products = {}
    with open('products.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for i in reader:
            products[i['name']] = Products(i['name'], i['price'], int(i['q_left']))
    return products
