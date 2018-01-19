# PushStocks
## Developed by Evan Quach.
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

**PushStocks** is a mobile notification python script that uses PushBullet to send a message when
a stock's quote has met a specified price. *this is a self-hosted script*

# Requirements:
* Python3
* BeautifulSoup4(bs4)
* PushBullet

# TODO:
* Create a .cfg to specify an array of symbols in a /data/ dir.
* Create a .cfg to specify a threshold (min. price) in a /data/ dir.
* Send messages for fatal errors and close prices.
* Pause or resume the script at market close/open times.
