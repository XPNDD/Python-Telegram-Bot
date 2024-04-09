import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()
    BOT_TOKEN = os.getenv('TOKEN')
    DEFAULT_COMMANDS = (('start', 'Начало работы с ботом'),
                        ('help', 'Список доступных команд'),
                        ('low', 'вывод минимальных показателей'),
                        ('high', 'вывод максимальных показателей'),
                        ('custom', 'вывод показателей пользовательского диапазона'),
                        ('history', 'вывод истории запросов'))
