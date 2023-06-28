import requests
from bs4 import BeautifulSoup
import random
import csv
from config import headers  # my "user agent" and "accept"

URL = "https://vedmak.fandom.com/wiki/%D0%A1%D0%B0%D0%BB%D1%8C%D0%BC%D0%B0"


proxy_tor = "socks5://127.0.0.1:" + str(random.randint(9052, 9139))
proxies = {"https": proxy_tor}

FILENAME = 'WitcherBook'


with open("index.html", "r") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")


def parse_beast_class(soup_obj):
    beast_class = soup_obj.find("div", {'data-source': "Класс"}).find("a").get("title")
    return beast_class


def parse_beast_variation(soup_obj):
    beast_variation = soup_obj.find("div", {'data-source': "Вид"}).find("a").get("title")
    return beast_variation


def parse_beast_type(soup_obj):
    beast_type = soup_obj.find("div", {'data-source': "Тип"}).find("div").text
    return beast_type


def parse_beast_location(soup_obj):
    beast_location = soup_obj.find("div", {'data-source': "Местонахождение"}).find("div").text
    return beast_location


def parse_beast_tactic(soup_obj):
    try:
        beast_tactic = soup_obj.find("div", {'data-source': "Тактика"}).find("div").text
        return beast_tactic
    except AttributeError:
        return "Нет данных"
# there may be no tactic (exception AttributeError)


def parse_beast_weakness(soup_obj):
    res = []
    beast_weakness = soup_obj.find("div", {'data-source': "Уязвимость"}).find("div").find_all("a")
    for weak in beast_weakness:
        res.append(weak.text)
    return res


print(parse_beast_weakness(soup))

