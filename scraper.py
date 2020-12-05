import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/Mark-III-mit-24-105-ILCE7M3GBDI/dp/B07RCHY5M4/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=sony+a7&qid=1607199872&quartzVehicle=5-672&replacementKeywords=sony&sr=8-1'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())
    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = price[0:5]
    converted_price = float(converted_price)

    if converted_price < 1700:
        send_mail()

    # print(title.strip())
    # print(type(converted_price))
    # print(converted_price)

    if converted_price > 1700:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # etablish connection between two emails
    server.starttls()  # encrypt email
    server.ehlo()

    server.login('bessamhajsalem@gmail.com', 'uaxarepnsgvtictm')

    subject = 'Price fell down!'
    body = 'check the amazon link https://www.amazon.de/Mark-III-mit-24-105-ILCE7M3GBDI/dp/B07RCHY5M4/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=sony+a7&qid=1607199872&quartzVehicle=5-672&replacementKeywords=sony&sr=8-1'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'bessamhajsalem@gmail.com',
        'bessamhadjsalem@yahoo.com',
        msg
    )
    print('Hey Email has been sent')

    server.quit()  # close connection


check_price()
# while True:
#     check_price()
#     time.sleep(86400)
