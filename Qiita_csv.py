import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import datetime	

url = 'https://qiita.com/advent-calendar/2016/crawler'
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")
elems = soup.select('.adventCalendarItem_entry a')

elem_list = []
url_list = []

for i in elems:
    elem_list.append(i.text)
    url_list.append(i.attrs['href'])

df_title_url = pd.DataFrame({'Title':elem_list, 'URL':url_list})
print(df_title_url)

df_title_url.to_csv('Qiita_csv04.csv',encoding='shift jis')