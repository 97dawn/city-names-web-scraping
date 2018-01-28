'''
Created on Jan 27, 2018

@author: user
'''
from lxml import html
import requests

page = requests.get('https://en.wikipedia.org/wiki/List_of_cities_in_South_Korea')
tree = html.fromstring(page.content)
cities = tree.xpath('//span[@lang="ko"]/text()')
cities=cities[15:]
updateCities=[]
for i in range(len(cities)):
    if i % 2 == 0:
        updateCities.append(cities[i])
