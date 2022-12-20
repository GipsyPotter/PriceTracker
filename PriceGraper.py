import requests
from bs4 import BeautifulSoup


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
    return rprice


def TGDD(URL):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    rprice = ""
    page = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all("div", class_="oo-left")
    for result in results:
        price = result.find("strong")
        price = price.text.strip()
        for digit in price:
            if digit.isnumeric():
                rprice += str(digit)
    return rprice


if __name__ == "__main__":
    URL = "https://www.thegioididong.com/laptop/hp-240-g8-i3-617k6pa"
    print(TGDD(URL))
