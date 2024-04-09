import requests


def items_req(url):
    response = requests.get(url).json()
    items_lst = []
    for item in response:
        item_info = {
            'id': item['id'],
            'title': item['title'],
            'price': item['price'],
            'category': item['category'],
            'description': item['description'],
            'image': item['image']
        }
        items_lst.append(item_info)
    return items_lst
