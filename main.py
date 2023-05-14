import telebot
import requests
from bs4 import BeautifulSoup
import time
import datetime
from datetime import timedelta

token = '6232359107:AAEphBDT4Agc__vH89H60F8RIuVJwnQsD1g'
chat_id = '-1001932935606'
d = datetime.datetime.today()

day = d.strftime("%d")
month = d.strftime("%m")
year = d.strftime("%Y")
hour = d.strftime("%H")
minute = d.strftime("%M")
second = d.strftime("%S")

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
data = {'PHPSESSID': '8unnqr727fncndiao340530rk3'}


def first_day():
    print('first func is work')
    stroke = day + '-' + month + '-' + year + '+' + hour + '%3A' + minute + '%3A' + second

    bot = telebot.TeleBot(token)

    url = 'http://cab2.ru/sched.php?date=' + stroke

    s = requests.Session()

    f = open('orders.txt', 'a')
    a = 1
    file = open('orders.txt')
    all_words = []
    line = file.readlines()
    while line:
        all_words.extend(line)
        line = file.readlines()

    while a == 1:
        r = s.get(url, headers=headers, cookies=data)
        content = r.content.decode(encoding='utf-8')
        soup = BeautifulSoup(content, 'html.parser')

        orders = []
        title = soup.findAll('a', {'target': '_blank'})
        for i in title:
            orders.append(i.text)

        if title is not None:
            for i in title:
                order = i.text
                print(order)

                if order + '\n' not in all_words:
                    f.write(order + '\n')
                    all_words.append(order + '\n')
                    text = 'Pizduy delat work №' + order
                    bot.send_message(chat_id, text)
                    print('New order')
                    time.sleep(20)
                    continue
                else:
                    print('Order is already have')
                    time.sleep(20)

        else:
            print('Order is not have')
            time.sleep(20)


first_day()
