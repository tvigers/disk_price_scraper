#!/usr/bin/python
import requests
import json
from bs4 import BeautifulSoup
from prettytable import PrettyTable

data_file = "./disks.json"
json_file = open(data_file, "r")
data_load = json.load(json_file)

table = PrettyTable()
table.title = 'Disk Prices'
table.field_names = ['Vendor', 'SKU', 'Description', 'Price', 'URL']
table.align["Vendor"] = "l"
table.align["SKU"] = "r"
table.align["Description"] = "l"
table.align["Price"] = "r"
table.align["URL"] = "l"

for item in data_load['scorptec']:
  vendor = item['vendor']
  size_string = item['size_string']
  url = item['url']
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  product = soup.find('h1', {'id' : 'product_name'}).text.split(',')
  price = soup.find('div', {'id' : 'price-price'}).text.split()
  table.add_row([vendor, product[1], product[0], price[0], url])

print(table)
