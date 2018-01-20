# PushStocks v2.0 release

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

**PushStocks** is a mobile notification python script developed by Evan Quach that uses PushBullet to send a message when a stock's quote has met a specified price. *This is a self-hosted script.* Now with cryptocurrency as well!.

# Requirements:
* [Python3](https://www.python.org)
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
* [PushBullet](https://www.pushbullet.com)

# TODO:
* Send messages for fatal errors and close prices.
* Save api key
* Pause or resume the script at market close/open times.
* Use different url source for get_rate (i.e., [Binance](https://www.binance.com/tradeDetail.html?symbol=XLM_BTC) or [gdax](https://www.gdax.com/trade/BTC-USD))
* Add more exception catching and re-organize duplicate codes.

# Installation:
1) Install Python3 (Check the box for **add to os environmental variable** for Windows)
2) Download/clone this repo to a directory.
3) Navigate to that directory using `cd` and type `pip install -r requirements.txt` in the terminal.
4) Double click on pushstocks.py (for Windows) or type `python3 pushstocks.py` into the terminal.

*Optional* Clone this repo using git to keep it updated.
