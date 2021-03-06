import sys
sys.path.insert(0, "lib")
import re
import time
import datetime
from urllib.request import urlopen

try:
    from bs4 import BeautifulSoup
    from pushbullet import PushBullet
except ImportError:
    print("Requirements were not installed. Please consult guide at\n"
          "https://github.com/evanq123/PushStocks \n")
    sys.exit(1)

use_crypto = True
answer = input("Enter 's' for stock, or 'c' for crypto.")
if answer is 's':
    use_crypto = False
if use_crypto is True:
    currency    = input("Enter the currency(full name): ").upper()
    threshold   = float(input("Enter the amount in BTC to start notifying: "))
else:
    symbol      = input("Enter the symbol: ").upper()
    threshold   = float(input("Enter the amount in USD to start notifying: "))
api_key     = input("Enter your PushBullet api key: ")
intervals   = int(input("Enter the time (in seconds) between checks: "))


def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    url = urlopen(base_url + symbol)
    soup = BeautifulSoup(url, "html.parser")
    quote = soup.find('span', attrs={'class': 'pr'}).text
    return quote


def get_rate(currency): #This works, but is very slow
    currency = currency.replace(" ", "-")
    base_url = 'http://coinmarketcap.com/currencies/'
    url = urlopen(base_url + currency + "/")
    soup = BeautifulSoup(url, "html.parser")
    rate = soup.find('span', attrs={"class": "text-gray details-text-medium"}).text
    return rate


def push_message(msg):
    pb = PushBullet(api_key)
    if use_crypto is True:
        pb.push_note("PushStocks: The rate for {} has changed!".format(currency), msg)
    else:
        pb.push_note("PushStocks: The quote for {} has changed!".format(symbol), msg)


message_sent = False # Hackish workaround for now.
def price_past_threshold():
    non_decimal = re.compile(r'[^\d.]+')
    if use_crypto is True:
        data = get_rate(currency)
    else:
        data = get_quote(symbol)

    value = non_decimal.sub('', data)
    if float(value) >= float(threshold):
        return True


while True:
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if price_past_threshold() and message_sent is False:
        if use_crypto is True:
            msg = ("As of, {} EST, the rate for {} is >= {} BTC (at {})"
                   "".format(date, currency, threshold, get_rate(currency)))
        else:
            msg = ("As of, {} EST, the quote for {} is >= {} USD (at {} USD)"
                   "".format(date, symbol, threshold, get_quote(symbol).strip('\n')))

        print("Sending message to PushBullet...\n")
        push_message(msg)
        message_sent = True

    if not price_past_threshold() and message_sent is True:
        if use_crypto is True:
            msg = ("As of, {} EST, the rate for {} is < {} BTC (at {})"
                   "".format(date, currency, threshold, get_rate(currency)))
        else:
            msg = ("As of, {} EST, the quote for {} is < {} USD (at {} USD)"
                   "".format(date, symbol, threshold, get_quote(symbol)))
        print("Sending message to PushBullet...\n")
        push_message(msg)
        message_sent = False

    time.sleep(intervals)
