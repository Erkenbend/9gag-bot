import datetime
from pyquery import PyQuery
import json

from meme_maker.make_meme import make_meme

make_meme('2000-02-28', '2000-05-06', '../meme_maker/resources/ImageLibrary/dead_person.jpg')

exit(123)

class DeadPerson:
    def __init__(self, year, name, wiki_url, text_length):
        self.year = year
        self.name = name
        self.wiki_url = wiki_url
        self.text_lenght = text_length

class JsonWrapper:
    def __init__(self, dead_persons):
        self.dead_persons = dead_persons

# build wiki url
today = datetime.datetime.now()
month = today.strftime("%B")
day = int(today.strftime("%d")) + 1
url = f"https://en.wikipedia.org/wiki/{month}_{day}#Deaths"
print(url)

# query page
pq = PyQuery(url)
tag = pq('#Deaths').parent().next("ul")

childs = tag.children()
dead_persons = []

for child in childs:
    links = child.findall("a")
    #print(links)

    if len(links) >= 2: 
        year = links[0].text_content()
        try:
            if int(year) >= 1990:
                name = links[1].text_content()
                p_url = f"https://en.wikipedia.org{links[1].attrib.get('href')}"
                text = PyQuery(p_url).text() # => costs time
                text_length = len(text)
                dead_persons.append(DeadPerson(year, name, p_url, text_length))
        except ValueError:
            continue

print("parsed all dead persons")

def sort_by_text_lenght(e):
    return e.text_lenght

dead_persons.sort(reverse=True,key=sort_by_text_lenght)

print(dead_persons[0].__dict__)
jsonArray = []
for dp in dead_persons:
    #print(dp.text_lenght)
    jsonArray.append(dp.__dict__)

jsonstr = json.dumps(JsonWrapper(jsonArray).__dict__)
#print(jsonstr)