# Bitly url shorterer

This program for create short link from your url. And you can also see how many attempts were made to access through short links.

### How to install

Register and get a token on the site [bit.ly](https://bit.ly/). Save the received token in the file ".env" under name BITLY_TOKEN. example:
```
BITLY_TOKEN="..."
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
## Run

Launch on Linux(Python 3) or Windows:

```sh
$ python3 main.py http://ya.ru
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).