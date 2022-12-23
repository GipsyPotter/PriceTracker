import requests
from bs4 import BeautifulSoup


def Pformat(price): #Format the price
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
    #Need to add headers to avoid 403 error
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


def Phongvu(URL):
    rprice = ""
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("div", class_="att-product-detail-latest-price")
    for result in results:
        result = result.text.strip()
        for digit in result:
            if digit.isnumeric():
                rprice += str(digit)
    return Pformat(rprice)


def main(): #Check if the URL is valid
    URL = input("URL: ")
    if "cellphones.com.vn" in URL:
        print(Cellphones(URL))
    elif "thegioididong.com" in URL:
        print(TGDD(URL))
    elif "gearvn.com" in URL:
        print(GearVN(URL))
    elif "phongvu.vn" in URL:
        print(Phongvu(URL))
    else:
        print("URL not supported")



if __name__ == "__main__":
    main()
    #For now, the program only scrapes the main price if it finds
    #multiple prices on the page. I'll add a feature to choose