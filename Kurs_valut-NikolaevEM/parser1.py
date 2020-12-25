from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

def create_csv(data):
    columns=['date', 'value']

    with open("data3.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
        for i in data:
            file_writer.writerow(i)

        #df = pd.DataFrame(data, columns=columns)
        #df.to_csv('data2.csv')

def parse(date):
    URL = 'https://cbr.ru/eng/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To='+date
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 YaBrowser/20.11.3.183 Yowser/2.5 Safari/537.36',
    'accept': '*/*'}

    responce = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(responce.content, 'html.parser')
    items = soup.findAll('td')
    #print("k")
    #print(items)

    flag = False

    for item in items:
        if flag:
            return item.get_text(strip = True)
        if item.get_text(strip = True) == "US Dollar":
            flag = True

    return 1

    #print("\n\n")
    #print(data)
            
##        count = 0
##        i=0
##    for item in items:
##        if count==5:
##            count = 0
##            i+=1
##        if count==0:
##            data.append([])
##        data[i].append(item.get_text(strip = True))
##        count+=1
##        print(data)
##        print("\n\n")
##        if i==3:
##            break;
    
data = []
days =[]
days = pd.date_range('2020-11-25', '2020-12-25', freq='D')

i=0
for day in days:
    data.append([])
    data[i].append(str(day)[:10])
    print(str(day)[:10])
    #print((str(day)[8:-9]+"%2F"+str(day)[5:7]+"%2F"+str(day)[:4]))
    data[i].append(parse(str(day)[8:-9]+"%2F"+str(day)[5:7]+"%2F"+str(day)[:4]))
    i+=1

print(data)
create_csv(data)

