from bs4 import BeautifulSoup
import requests

#URL = 'https://www.olx.kz/elektronika/kompyutery-i-komplektuyuschie/'
URL = 'https://yandex.ru/news/quotes/2002.html'
#URL = 'https://www.finanz.ru/valyuty/v-realnom-vremeni'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 YaBrowser/20.11.3.183 Yowser/2.5 Safari/537.36',
    'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'news-stock-table__content')

    #print(items)

    kurs = []
    for item in items:
        kurs.append({
            'title': item.find_all('div', class_='news-stock-table__row news-stock-table__row_change_positive news-stock-table__row_today')
            #'item' : item.find('p', class_='rate')
        });
    print(kurs)
    print(len(kurs))



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