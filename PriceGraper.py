import requests
from bs4 import BeautifulSoup


def Pformat(price):
    if price:
        price = int(price)
        price = "{:,}".format(price)
        return price
    else:
        return "Price not found"


def Cellphones(URL):
    rprice = ""
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="layout-desktop")
    # print(results.prettify())
    prices = results.find_all("p", class_="product__price--show")
    for price in prices:
        price = price.text.strip()
        for digit in price:
            if digit.isnumeric():
                rprice += str(digit)
    return Pformat(rprice)


def TGDD(URL):
    tag = input("Tag: ")
    Class = input("Class: ")

    if not tag or not Class:
        tag = "p"
        Class = "box-price-present"

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    rprice = ""
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all(tag, class_=Class)
    for result in results:
        result = result.text.strip()
        for digit in result:
            if digit.isnumeric():
                rprice += str(digit)
    return Pformat(rprice)


def GearVN(URL):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    rprice = ""
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("span", class_="product_sale_price")
    if not results:
        results = soup.find_all("span", class_="product_price")
    for result in results:
        result = result.text.strip()
        for digit in result:
            if digit.isnumeric():
                rprice += str(digit)
    return Pformat(rprice)



if __name__ == "__main__":
    URL = "https://gearvn.com/products/ban-phim-co-fl-esports-cmk87sam-tropical-forest"
    print(GearVN(URL))
