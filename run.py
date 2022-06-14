import os
from bs4 import BeautifulSoup
from pyairtable import Table

table = Table('${AIRTABLE_API_KEY}', 'appXWUutxjHAwRkJ1', 'Students')

f0 = open("./pages/student-directory.txt", "r")
f1 = open("./pages/12-favorite-problems.txt", "r")
f2 = open("./pages/faq-piece.txt", "r")
f3 = open("./pages/unique-perspective.txt", "r")
f4 = open("./pages/coin-a-phrase.txt", "r")
f5 = open("./pages/curation-piece.txt", "r")
f6 = open("./pages/your-writing-system.txt", "r")

records = {} 
# {Alice: {Name: Alice, Assignments: [12 Fav, FAQ], Title: XYZ}

# Initial Setup
soup = BeautifulSoup(f0.read(), "html.parser")
soup = soup.find("div", class_="infinite-scroll-component")
results = soup.find_all("div", attrs={'class':'community-member'})

for result in results:
    name = result.find("div", class_="community-member__title").find("h3").text
    records[name] ={'Name':name, 'Assignment':[], 'FAQ Piece':'', 'Unique Perspective':'','Coin a Phrase':'', 'Curation Piece':'', 'Your Writing System':''}

# Update Assignments

soup = BeautifulSoup(f1.read(), "html.parser")
soup = soup.find("div", class_="infinite-scroll-component")
results = soup.find_all("div", attrs={'class':'post--parent'})

for result in results:
    name = result.find("div", class_="author__name").text
    if result.find("div", class_="post__header") is None:
        title = ""
    else:
        title = result.find('div', class_='post__header').find('h2').text
    if name in records:
        records[name]['Assignment'].append('12 Favorite Problems')

soup = BeautifulSoup(f2.read(), "html.parser")
soup = soup.find("div", class_="infinite-scroll-component")
results = soup.find_all("div", attrs={'class':'post--parent'})

for result in results:
    name = result.find("div", class_="author__name").text
    if result.find("div", class_="post__header") is None:
        title = ""
    else:
        title = result.find('div', class_='post__header').find('h2').text
    if name in records:
        records[name]['FAQ Piece'] = title 
        records[name]['Assignment'].append('FAQ Piece')

soup = BeautifulSoup(f3.read(), "html.parser")
soup = soup.find("div", class_="infinite-scroll-component")
results = soup.find_all("div", attrs={'class':'post--parent'})

for result in results:
    if result.find("div", class_='author__name') is not None:
        name = result.find("div", class_="author__name").text
    if result.find("div", class_="post__header") is None:
        title = ""
    else:
        title = result.find('div', class_='post__header').find('h2').text
    if name in records:
        records[name]['Unique Perspective'] = title 
        records[name]['Assignment'].append('Unique Perspective')

soup = BeautifulSoup(f4.read(), "html.parser")
soup = soup.find("div", class_="infinite-scroll-component")
results = soup.find_all("div", attrs={'class':'post--parent'})

for result in results:
    name = result.find("div", class_="author__name").text
    if result.find("div", class_="post__header") is None:
        title = ""
    else:
        title = result.find('div', class_='post__header').find('h2').text
    if name in records:
        records[name]['Coin a Phrase'] = title 
        records[name]['Assignment'].append('Coin a Phrase')

soup = BeautifulSoup(f5.read(), "html.parser")
soup = soup.find("div", class_="infinite-scroll-component")
results = soup.find_all("div", attrs={'class':'post--parent'})

for result in results:
    name = result.find("div", class_="author__name").text
    if result.find("div", class_="post__header") is None:
        title = ""
    else:
        title = result.find('div', class_='post__header').find('h2').text
    if name in records:
        records[name]['Curation Piece'] = title 
        records[name]['Assignment'].append('Curation Piece')

soup = BeautifulSoup(f6.read(), "html.parser")
soup = soup.find("div", class_="infinite-scroll-component")
results = soup.find_all("div", attrs={'class':'post--parent'})

for result in results:
    name = result.find("div", class_="author__name").text
    if result.find("div", class_="post__header") is None:
        title = ""
    else:
        title = result.find('div', class_='post__header').find('h2').text
    if name in records:
        records[name]['Your Writing System'] = title 
        records[name]['Assignment'].append('Your Writing System')

entries = list(records.values())

table.batch_create(entries)
