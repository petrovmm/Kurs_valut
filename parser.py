from bs4 import BeautifulSoup
import requests

#URL = 'https://yandex.ru/news/quotes/1.html'
#URL = 'https://www.x-rates.com/table/?from=USD&amount=1'
URL = 'https://www.banki.ru/products/currency/cash/yakutsk/'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 YaBrowser/20.11.3.183 Yowser/2.5 Safari/537.36',
    'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    #items = soup.find_all('div', class_ = 'news-stocks__stock mg-grid__item Theme Theme_color_yandex-default Theme_size_default Theme_capacity_default Theme_space_default Theme_cosmetic_default')
    items = soup.findAll('tr', class_ = 'currency-table__bordered-row')
    #print(items)
 
    kurs = []
    for item in items:
        kurs.append({
            'title': item.find('td', class_='currency-table__large-text color-turquoise').get_text(strip = True),
            'item' : item.find('div', class_='currency-table__large-text').get_text(strip = True)
        });
        for kur in kurs:
            print(kur['item'])

    #print(kurs)
    #print(len(kurs))



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')
"""""
    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findALL('div',class_ = 'offer-wrapper')
    comps = []

    for item in items:
        comps.append({
            #'title':item.find('a', class_ = 'marginright5 link linkWithHash detailsLink linkWithHashPromoted').get_text(strip = True)
            'title':item.find('a', class_='marginright5 link linkWithHash detailsLink linkWithHashPromoted').get_text(strip = True)
        })

        for comp in comps:
            print(comp['title'])
            """""
parse()