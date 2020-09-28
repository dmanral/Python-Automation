import bs4, requests

# Doesnt actually work on Amazon anymore.
def getAmazonPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#bundle > div:nth-child(3) > div.product-page.product-page--nordstromrack > div.product-page__row > div.product-page__details > section > div.product-details__pricing-and-style > div.pricing-and-style > div > div.pricing-and-style__sale > span.pricing-and-style__sale-price.pricing-and-style__sale-price--clearance')
    return elems[0].text.strip()

price = getAmazonPrice('https://www.nordstromrack.com/shop/product/2765110/ben-sherman-bristol-slip-on-sneaker?color=NATURAL%20CA')
print('The price is ' + price)
