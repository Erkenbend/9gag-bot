# 9gag-bot

## Original goal

We wanted to create a piece of code that could run once a day and post a pic on 9gag of
the most well-know person which had their death anniversary.

This would be created in the timeframe of one evening and would later be hosted somewhere
in the Cloud.

## Deviation

As we realized that automatic 9gag posting was pretty hard (because of lack of an official
API, use of Captchas, and Cloudflare DDOS protection on login), we switched to posting it
on Twitter: see [@RipBot__](https://twitter.com/RipBot__).

This is also not cloud-ready yet, we may update this later.

## Actual functionality

This project consists in 3 parts, that are stored in their corresponding python files and
run one after the other in `main.py`:
* `wiki_search.py`: parse Wikipedia content for the page of a given date and
return the person who died on this day along with meta-infos (like, date of birth, link to
picture)
* `make_meme.py`: use the meta-info and the `MemePy` library to add text onto the image
* `upload_twitter.py`: tweet the generated image along with a standard text.

Other scripts:
* `upload.py` (broken): login to 9gag and upload a pic using a selenium-controlled browser; this
is implemented up to the point where you have to choose categories
* `login_to_twitter`: refresh the tokens that are being used by `upload_twitter.py`

## How to use

### Requirements

To run this app, you need:
* Python 3.6+
* Twitter API-key details under `resources/twitter_credentials.yml`

To use the unfinished 9gag upload feature, you need:
* 9gag credentials as `username:password` under `resources/credentials.txt`

Make sure you have all the needed dependencies by running `pip install -r requirements.txt`

### Running the code

Simply change the date in `main.py` to the desired day and run `python main.py`
