#%%
# dowlonad file using request
from urllib.request import urlretrieve

url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
urlretrieve(url, 'data_science/wine_data.csv')

#%%

# download file using requests

import requests

url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
r = requests.get(url, allow_redirects=True)
open('google.csv', 'wb').write(r.content)
#%%
# requests to get html data

import requests
from bs4 import BeautifulSoup

url = 'https://campus.datacamp.com/courses/intermediate-importing-data-in-python/importing-data-from-the-internet-1?ex=6'
response = requests.get(url)
text = response.text

# we can pretty the text using BeautifulSoup
pretty = BeautifulSoup(text)
print(pretty.prettify())

# get the title
title = pretty.title
text = pretty.get_text()

print(title)
print(text)

# You can use find_all to get a particular tags
h1 = pretty.find_all('h1')

for header in h1:
    print(header.text)

a = pretty.find_all('a')

for link in a:
    print(link.get('href')) # .get() method to extract the attributes of a tag