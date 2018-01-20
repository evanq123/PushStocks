import sys
sys.path.insert(0, "lib")
import time
from datetime import datetime
from urllib.request import urlopen

try:
    from bs4 import BeautifulSoup
    from pushbullet import PushBullet
except ImportError:
    print("Requirements were not installed. Please consult guide at\n"
          "https://github.com/evanq123/PushStocks \n")
    sys.exit(1)

use_crypto = True # Default, another hackish method to improve later.
answer = input("Type 's' for stock mode, else 'c' for crypto")
if answer is 's':
    use_crypto = False

api_key         = input("Enter your PushBullet api key: ")
if use_crypto:
    currency    = input("Enter the currency(full name): ").upper()
    threshold   = float(input("Enter the amount in BTC to start notifying: "))
else:
    symbol      = input("Enter the symbol: ").upper()
    threshold   = float(input("Enter the amount in USD to start notifying: "))
intervals       = int(input("Enter the time intervals (s) between checks: "))

def get_rate(currency): #This works, but is very slow
    currency = currency.replace(" ", "-")
    base_url = 'http://coinmarketcap.com/currencies/'
    url = urlopen(base_url + currency + "/")
    soup = BeautifulSoup(url, "html.parser")
    rate = soup.find('span', attrs={"class": "text-gray details-text-medium"}).text
    return rate


def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    url = urlopen(base_url + symbol)
    soup = BeautifulSoup(url, "html.parser")
    quote = soup.find('span', attrs={'class': 'pr'}).text
    return quote


def push_message(msg):
    pb = PushBullet(api_key)
    if use_crypto:
        pb.push_note("PushStocks: The rate for {} has changed!".format(currency), msg)
    else:
        pb.push_note("PushStocks: The quote for {} has changed!".format(symbol), msg)


message_sent = False # Hackish workaround for now.
def price_past_threshold():
    non_decimal = re.compile(r'[^\d.]+')
    quote = non_decimal.sub('', get_quote(currency))
    if float(quote) >= float(threshold):
        return True


while True:
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if price_past_threshold() and message_sent is False:
        if use_crypto:
            msg = ("As of, {} EST, the rate for {} is >= {} BTC (at {} BTC)"
                   "".format(date, currency, threshold, get_quote(currency)))
            print("Sending message to PushBullet...\n")
            push_message(msg, currency)
        else:
            msg = ("As of, {} EST, the quote for {} is >= {} USD (at {} USD)"
                   "".format(date, symbol, threshold, get_quote(symbol).strip('\n')))
            print("Sending message to PushBullet...\n")
            push_message(msg, symbol)
        message_sent = True

    if not price_past_threshold() and message_sent is True:
        if use_crypto:
            msg = ("As of, {} EST, the rate for {} is < {} BTC (at {} BTC)"
                   "".format(date, currency, threshold, get_quote(currency)))
            print("Sending message to PushBullet...\n")
            push_message(msg, currency)
        else:
            msg = ("As of, {} EST, the quote for {} is < {} USD (at {} USD)"
                   "".format(date, symbol, threshold, get_quote(symbol)))
            print("Sending message to PushBullet...\n")
            push_message(msg, symbol)
        message_sent = False

    time.sleep(intervals)
