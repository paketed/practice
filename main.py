import requests
from bs4 import BeautifulSoup as BS


def search():
    count = 0
    while 1:
        name = input('Для поиска введите название криптовалюты, для выхода — q: ')
        if name == 'q':
            return
        for item in open('C:\\Users\\drofa\\Desktop\\PY\\practice\\new.csv'):
            DATA = item.split(";")

            if DATA[0].lower() == name.lower():
                print("Стоимость 1 единицы:", DATA[1])
                print("Рыночная капитализация:", DATA[2])
                count += 1


def write_csv(data, f_name='new.csv'):
    with open(r"C:\Users\drofa\Desktop\PY\practice\new.csv", "a+") as file:
        file.write(data + '\n')
    file.close()
    return f_name

url = 'https://coinmarketcap.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/101.0.4951.54 Safari/537.36 '
           }

r = requests.get(url, headers = headers)
soup = BS(r.text, 'lxml')
trs = soup.find('tbody').find_all('tr', limit = 10)
name_f = []
price_f = []
market_cup_f = []
for tr in trs:
    quotes = tr.find_all('div', class_='sc-16r8icm-0 escjiH')
    names = tr.find_all('p', class_='sc-1eb5slv-0 iworPT')
    prices = tr.find_all('div', class_='sc-131di3y-0 cLgOOr')
    market_cups = tr.find_all('span', class_='sc-1ow4cwt-1 ieFnWP')
    for name in names:
        name_f.append(name.text)
    for price in prices:
        price_f.append(price.text)
    for market_cup in market_cups:
        market_cup_f.append(market_cup.text)
print(name_f)

with open(r"C:\Users\drofa\Desktop\PY\practice\new.csv", "w") as file:
    file.close()
for i in range(0, 10):
    print(name_f[i] + " " + price_f[i] + " " + market_cup_f[i])
    write_csv(name_f[i] + ";" + price_f[i] + ";" + market_cup_f[i])
print()
if __name__ == "__main__":
    search()
