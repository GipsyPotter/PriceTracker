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


if __name__ == "__main__":
    URL = "https://cellphones.com.vn/vong-deo-tay-thong-minh-xiaomi-mi-band-7.html"
    print(Cellphones(URL))
