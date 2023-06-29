import requests
from bs4 import BeautifulSoup
import random
import csv
from config import headers  # my "user agent" and "accept"

URL = "https://vedmak.fandom.com/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%9C%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%8B_(%D0%92%D0%B5%D0%B4%D1%8C%D0%BC%D0%B0%D0%BA_3)"

proxy_tor = "socks5://127.0.0.1:" + str(random.randint(9052, 9139))
proxies = {"https": proxy_tor}

FILENAME = 'WitcherBook'

# with open("index.html", "r") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "lxml")
# TODO:
"""
1) make main function to request page with monsters and collect info about every one
2) write this information to 'WitcherBook' csv file
"""


def parse_monster_characteristic(soup_obj, parameter):    # class, variation, species, type, location, tactic, resist, weakness
    try:
        res = ''
        monster_characteristic = soup_obj.find("aside",
                                               class_="portable-infobox pi-background "
                                                      "pi-border-color pi-theme-Ведьмак-3 pi-layout-default")
        if monster_characteristic is None:
            monster_characteristic = soup_obj.find("aside",
                                                   class_="portable-infobox pi-background "
                                                          "pi-border-color pi-theme-Каменные-сердца pi-layout-default")
        if monster_characteristic is None:
            monster_characteristic = soup_obj.find("aside",
                                                   class_="portable-infobox pi-background "
                                                          "pi-border-color pi-theme-Кровь-и-Вино pi-layout-default")
        if monster_characteristic is None:
            return
        if parameter == 'Имя':
            monster_characteristic = monster_characteristic.find("h2").text
            res = monster_characteristic
            return res
        else:
            monster_characteristic = monster_characteristic.find("div", {'data-source': parameter}).find("div")
            for el in monster_characteristic:
                res += el.text
            return res
    except AttributeError:
        return "Неизвестно"


def get_monster_name_and_link(soup_obj):
    links = {}
    allmonsters = soup_obj.find_all("div", class_="category-page__members-wrapper")
    for i in range(1, len(allmonsters)):
        monsters_curr_letter = allmonsters[i].find("ul")
        for monsters in monsters_curr_letter:
            monster = monsters.find("a")
            if str(monster) == '-1':
                pass
            elif monster.get("title") == "Монстры (Ведьмак 3)":
                pass
            else:
                links[monster.get("title")] = (monster.get("href"))
    return links


# print(len(get_monster_name_and_link(soup_obj=soup)))


def file_write_headers(filename):
    with open(f"{filename}.csv", "w", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(("Имя","Класс","Вид","Подвиды","Тип","Местонахождение","Тактика","Иммунитет", "Уязвимость"))


def file_write_data(filename, name, m_class, variation, species, m_type, location, tactic, resist, weakness):
    with open(f"{filename}.csv", "a", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow((name, m_class, variation, species, m_type, location, tactic, resist, weakness))


def main():
    url_first_part = '/'.join(URL.split('/')[:3])
    try:
        response = requests.get(url=URL, headers=headers, proxies=proxies)
        soup = BeautifulSoup(response.text)
        links = get_monster_name_and_link(soup_obj=soup)
        print("Перешли на главную страницу\nПолучили ссылки на страницы с монстрами")
        for name, link in links.items():
            monster_page = requests.get(url=url_first_part+link, headers=headers, proxies=proxies)
            monster = BeautifulSoup(monster_page.text)

    except
# def parse_beast_variation(soup_obj):
#     try:
#         beast_variation = soup_obj.find("aside",
#                                         class_="portable-infobox pi-background "
#                                                "pi-border-color pi-theme-Ведьмак-3 pi-layout-default")
#         beast_variation = beast_variation.find("div", {'data-source': "Вид"}).find("a").get("title")
#         return beast_variation
#     except AttributeError:
#         return "Нет данных о виде"
#
#
# def parse_beast_type(soup_obj):
#     try:
#         beast_type = soup_obj.find("aside",
#                                    class_="portable-infobox pi-background "
#                                           "pi-border-color pi-theme-Ведьмак-3 pi-layout-default")
#         beast_type = beast_type.find("div", {'data-source': "Тип"}).find("div").text
#         return beast_type
#     except AttributeError:
#         return "Нет данных о типе"
#
#
# def parse_beast_location(soup_obj):
#     beast_location = soup_obj.find("aside",
#                                    class_="portable-infobox pi-background "
#                                           "pi-border-color pi-theme-Ведьмак-3 pi-layout-default")
#     if beast_location is None:
#         beast_location = soup_obj.find("aside",
#                                        class_="portable-infobox pi-background "
#                                               "pi-border-color pi-theme-Кровь-и-Вино pi-layout-default")
#     if beast_location is None:
#         beast_location = soup_obj.find("aside",
#                                        class_="portable-infobox pi-background "
#                                               "pi-border-color pi-theme-Каменные-сердца pi-layout-default")
#     try:
#         beast_location = beast_location.find("div", {'data-source': "Местонахождение"}).find("div").text
#         return beast_location
#     except AttributeError:
#         return "Нет данных об обитании"
#
#
# def parse_beast_tactic(soup_obj):
#     try:
#         beast_tactic = soup_obj.find("aside",
#                                      class_="portable-infobox pi-background "
#                                             "pi-border-color pi-theme-Ведьмак-3 pi-layout-default")
#         beast_tactic = beast_tactic.find("div", {'data-source': "Тактика"}).find("div").text
#         return beast_tactic
#     except AttributeError:
#         return "Нет данных о тактике"
# # there may be no tactic (exception AttributeError)
#
#
# def parse_beast_resist(soup_obj):
#     try:
#         beast_resist = soup_obj.find("aside",
#                                      class_="portable-infobox pi-background "
#                                             "pi-border-color pi-theme-Ведьмак-3 pi-layout-default")
#         if beast_resist is None:
#             beast_resist = soup_obj.find("aside",
#                                            class_="portable-infobox pi-background "
#                                                   "pi-border-color pi-theme-Каменные-сердца pi-layout-default")
#         beast_resist = beast_resist.find("div", {'data-source': "Иммунитет"}).find("div").text
#
#         return beast_resist
#     except AttributeError:
#         return "Нет данных об иммунитете"
#
#
# def parse_beast_weakness(soup_obj):
#     try:
#         res = ''
#         beast_weakness = soup_obj.find("aside",
#                                        class_="portable-infobox pi-background "
#                                               "pi-border-color pi-theme-Ведьмак-3 pi-layout-default")
#         beast_weakness = beast_weakness.find("div", {'data-source': "Уязвимость"}).find("div").find_all("a")
#         for i in range(len(beast_weakness)):
#             res += beast_weakness[i].text
#             if i != len(beast_weakness) - 1:
#                 res += ', '
#         return res
#     except AttributeError:
#         return "Нет данных об уязвимостях"
