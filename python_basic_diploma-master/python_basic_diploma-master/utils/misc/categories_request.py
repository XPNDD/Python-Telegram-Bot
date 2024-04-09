import requests


def cat_req():
    response = requests.get('https://fakestoreapi.com/products/categories').json()
    categories_lst = list()
    for category in response:
        categories_lst.append(category)
    return categories_lst
