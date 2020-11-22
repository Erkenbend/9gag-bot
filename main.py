import datetime
from wiki_search import wiki_search
from make_meme import make_meme
from upload_twitter import upload_twitter

def main():
    dead_person = wiki_search(datetime.datetime(2020, 6, 25))
    make_meme(dead_person.bday, dead_person.dday, "./resources/ImageLibrary/dead_person.jpg")
    upload_twitter(dead_person.name)

if __name__ == '__main__':
    main()
