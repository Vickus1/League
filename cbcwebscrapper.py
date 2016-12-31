import requests
from bs4 import BeautifulSoup
import html5lib

def linespace():
    print(" ")
    return;

def headlines(link):
    print(link)
    index = list()
    for i in range(len(link)):
        if link[i].get_text() == 'Home':
            index.append(i)
        print(index)
        return index;


URLbase = "http://www.cbc.ca/news"
a = "a"
b = "pinnableHref pinnableHeadline"
index = list()
page = requests.get(URLbase)
soup = BeautifulSoup(page.text, "html5lib")
link = soup.find_all('a', href=True)
textsearch = list()

search = input("Do you want to search anything specific? [y/n]: ")
search = search.lower()
while search!="y" and search!="n":
    search = input("Please enter [y/n]: ")

#for i in range(len(link)):
#    if link[i].get_text() == 'Home':
#        index.append(i)

#index = headlines(link)
for i in range(len(link)):
    if link[i].get_text() == 'Home':
        index.append(i)

#print(index)

if search == 'y':
    search = input("Please enter a word (Capital for names): ")
    for i in range(index[0]+1, index[1]-1):
        URL = URLbase+"/"+link[i].get_text()
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html5lib")
        for line in soup.find_all(a, {"class":b}):
            #print(link.get_text())
            if search in line.get_text():
                print(line.get_text())
                print("----------------------------------")
        
elif search == 'n':
    for i in range(index[0]+1, index[1]-1):
        print(link[i].get_text())
    test = input("Enter what type of news: ")
    linespace()
    URL= URLbase+"/"+test
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html5lib")
    print("CBC WORLD NEWS TOP STORIES")
    linespace()
    for link in soup.find_all(a, {"class":b}):
        #print(link.get_text())
        if "Carrie" in link.get_text():
            print(link.get_text())
            print("----------------------------------")
        
#print("CBC MOST VIEWS")
#linespace()
#for link in soup.find_all("li", {"class":"lineuproll-item-body"}):
#    print(link.get_text().replace("\t", "").replace("\s", "").replace("\n", ""))
#    print("----------------------------------")


