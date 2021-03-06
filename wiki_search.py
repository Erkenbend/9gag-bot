import datetime
from pyquery import PyQuery
import json
import requests
from make_meme import make_meme

class DeadPerson:
    def __init__(self, dday, name, wiki_url, text_length, img_url, bday):
        self.dday = dday
        self.name = name
        self.wiki_url = wiki_url
        self.text_length = text_length
        self.img_url = img_url
        self.bday = bday

class JsonWrapper:
    def __init__(self, dead_persons):
        self.dead_persons = dead_persons

def sort_by_text_lenght(e):
    return e.text_length

def wiki_search(today):
    month = today.strftime("%B")
    day = int(today.strftime("%d"))
    url = f"https://en.wikipedia.org/wiki/{month}_{day}#Deaths"
    print(url)

    # query page
    pq = PyQuery(url)
    tag = pq('#Deaths').parent().next("ul")

    childs = tag.children()
    dead_persons = []

    for child in childs:
        links = child.findall("a")
        # print(links)

        if len(links) >= 2:
            year = links[0].text_content()
            name = links[1].text_content()
            p_url = f"https://en.wikipedia.org{links[1].attrib.get('href')}"
        else:
            year = child.text_content().split('–', 1)[0]
            name = links[0].text_content()
            p_url = f"https://en.wikipedia.org{links[0].attrib.get('href')}"
        try:
            if int(year) >= 1990:
                dday = f"{year}-{today.strftime('%m')}-{day}"
                print(p_url)
                p_site = PyQuery(p_url)
                text_length = len(p_site.text())  # => costs time
                img_site = f'https://en.wikipedia.org{p_site.find("table.infobox.vcard").find("a")[0].attrib.get("href")}'

                img_url = PyQuery(img_site).find("div#file").find("a")[0].attrib.get("href")
                img_url = f'https:{img_url}'
                print(img_url)

                bday = p_site.find("table.infobox.vcard").find("span.bday")[0].text
                dead_persons.append(DeadPerson(dday, name, p_url, text_length, img_url, bday))
        except ValueError as ve:
            # print(ve)
            continue
        except IndexError as ie:
            # print(ie)
            continue

    print("parsed all dead persons")

    dead_persons.sort(reverse=True, key=sort_by_text_lenght)

    print(dead_persons[0].__dict__)

    my_d_person = dead_persons[0]
    r = requests.get(my_d_person.img_url, allow_redirects=True)
    img_path = "./resources/ImageLibrary/dead_person.jpg"

    open(img_path, 'wb').write(r.content)
    #print("downloaded file. now start making meme")

    # make_meme(str(my_d_person.bday), str(my_d_person.dday), img_path)
    # make_meme('2000-02-28', '2000-05-05', './resources/ImageLibrary/dead_person.jpg')

    print("Finished")

    return my_d_person

if __name__ == '__main__':
    print(wiki_search(datetime.datetime.now()))

