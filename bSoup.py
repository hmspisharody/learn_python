import re
import requests
from bs4 import BeautifulSoup

#collect data from indices page

page = requests.get('https://wf4.myhcl.com/iTime/iTime/index.html?v=11#/TimeSheet')

soup = BeautifulSoup(page.text, 'html.parser')

indices_list = soup.find(class_ = 'it-totalTime bg-wh ng-binding ng-scope')

print(indices_list)


