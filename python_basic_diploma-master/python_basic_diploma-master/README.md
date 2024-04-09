Будет использована [Fake Store Api](https://fakestoreapi.com)
---
---

## Список команд бота:

### 1) /start - начинает работу пользователя с ботом. 
При вводе данной команды выводится приветствие и inline keyboard, который позволяет по нажатию вызвать любую другу команду
### 2) /help - выводит список всех доступных команд с кликабельным текстом для упрощения взаимодействия с ботом
### 3) /low - запрашивает по какой именно категории товаров будет производиться поиск, а также кол-во элементов, которые необходимо вывести.
Затем бот выводит список товаров выбранной категории, отсортированных по убыванию цены.
### 4) /high - запрашивает по какой именно категории товаров будет производиться поиск, а также кол-во элементов, которые необходимо вывести.
Затем бот выводит список товаров выбранной категории, отсортированных по возрастанию цены.
### 5) /custom - запрашивает по какой именно категории товаров будет производиться поиск, а также кол-во элементов, которые необходимо вывести, а также границы выборки (минимальную и максимальную цену)
Затем бот выводит список товаров выбранной категории, удовлетворяющих границам выборки по цене.
### 6) /history - выводит краткую историю запросов пользователя (последние 10 запросов)
Реализация данной команды планируется с помощью БД, в которой для каждого нового пользователя будет создаваться новый столбец (по Telegram-id), а в каждую новую строку будут записываться выбранные им команды с введенной доп. информацией. БД будет функционировать по принципу FIFO (first-in, first-out)
### Endpoints:

[Пример ссылки для запроса (request)](https://fakestoreapi.com/products/categories) для получения списка доступных категорий товаров.
```python
import requests

response = requests.get('https://fakestoreapi.com/products/categories').json()
```
В ответ мы получаем список всех категорий товаров
```
electronics
jewelery
men's clothing
women's clothing
```
[Пример ссылки для запроса (request)](https://fakestoreapi.com/products/category/jewelery) для получения списка товаров выбранной категории.
```python
import requests

response = requests.get('https://fakestoreapi.com/products/category/jewelery').json()
```
В ответ мы получаем список всех товаров данной категории.
```
{'id': 5, 'title': "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet", 'price': 695, 'description': "From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.", 'category': 'jewelery', 'image': 'https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_.jpg', 'rating': {'rate': 4.6, 'count': 400}}
{'id': 6, 'title': 'Solid Gold Petite Micropave ', 'price': 168, 'description': 'Satisfaction Guaranteed. Return or exchange any order within 30 days.Designed and sold by Hafeez Center in the United States. Satisfaction Guaranteed. Return or exchange any order within 30 days.', 'category': 'jewelery', 'image': 'https://fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_.jpg', 'rating': {'rate': 3.9, 'count': 70}}
{'id': 7, 'title': 'White Gold Plated Princess', 'price': 9.99, 'description': "Classic Created Wedding Engagement Solitaire Diamond Promise Ring for Her. Gifts to spoil your love more for Engagement, Wedding, Anniversary, Valentine's Day...", 'category': 'jewelery', 'image': 'https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg', 'rating': {'rate': 3, 'count': 400}}
{'id': 8, 'title': 'Pierced Owl Rose Gold Plated Stainless Steel Double', 'price': 10.99, 'description': 'Rose Gold Plated Double Flared Tunnel Plug Earrings. Made of 316L Stainless Steel', 'category': 'jewelery', 'image': 'https://fakestoreapi.com/img/51UDEzMJVpL._AC_UL640_QL65_ML3_.jpg', 'rating': {'rate': 1.9, 'count': 100}}
```
#### P.S. Реализация команды /history может измениться в ходе написания кода (но это вряд ли)