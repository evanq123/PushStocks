# PushStocks v2.0 & PushCrypto v2.1

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

**PushStocks** is a mobile notification python script developed by Evan Quach that uses PushBullet to send a message when a stock's quote has met a specified price. *This is a self-hosted script*
Now with cryptocurrency as well!.

# Requirements:
* [Python3](https://www.python.org)
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
* [PushBullet](https://www.pushbullet.com)

# TODO:
* Send messages for fatal errors and close prices.
* Save api key
* Pause or resume the script at market close/open times.
* Create an installer.
* Update readme for pushcrypto.py
* Create a requirements.txt
* Use different for get_rate (i.e., [Binance](https://www.binance.com/tradeDetail.html?symbol=XLM_BTC) or [gdax](https://www.gdax.com/trade/BTC-USD)

# Installation:
1) Install Python3 (Check the box for **add to os environmental variable** for Windows)
2) Type `pip install beautifulsoup4` in the command window.
3) Type `pip install pushbullet.py` in the command window.
4) Download/clone this repo to a directory.
5) Change directories using `cd` and type `python3 pushstocks.py` into the command window.

*Optional* Clone this repo using git to keep it updated.
