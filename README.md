# PushStocks v0.1a

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

**PushStocks** is a mobile notification python script developed by Evan Quach that uses PushBullet to send a message when a stock's quote has met a specified price. *This is a self-hosted script*

# Requirements:
* [Python3](https://www.python.org)
* [BeautifulSoup4](beautifulsoup4 download)
* [PushBullet](https://www.pushbullet.com)

# TODO:
* Create a .cfg to specify an array of symbols in a /data/ dir.
* Create a .cfg to specify a threshold (min. price) in a /data/ dir.
* Send messages for fatal errors and close prices.
* Pause or resume the script at market close/open times.
* Create an installer.

# Installation:
1) Install Python3 (Check **add to os environmental variable** for Windows)
2) Type `pip install beautifulsoup4` in the command window.
3) Type `pip install pushbullet.py` in the command window.
4) Download/clone this repo to a directory.
5) Change directories using `cd` and type `python3 pushstocks.py` into the command window.
*Optional* Clone this repo using git to keep it updated.
