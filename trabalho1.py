import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from urllib.error import HTTPError



while True:
    url = 'https://books.toscrape.com/catalogue/page-1.html'
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'html.parser')
    except HTTPError as e:
        print('HTTP error')
    else:
        bookList = bs.find_all('article', class_='product_pod')
        with open('booksList.txt', 'w') as f:
            f.write(f"Título  -  Preço")

            for book in bookList:
                title = book.h3.a['title']
                price = book.select('.price_color')[0].get_text()
                price_regex = re.search(r'(\£[1-2][\d]*).([\d]{2})', price)

                if price_regex:
                    f.write(f"\n{title}, {price}\n")
                    print("\nTitle:", title,"\nPrice", price)
    time.sleep(3)