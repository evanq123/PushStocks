import sys
sys.path.insert(0, "lib")
import requests
import re
import time
import datetime

try:
    from bs4 import BeautifulSoup
    from pushbullet import PushBullet
except ImportError:
    print("Requirements were not installed. Please consult guide at\n"
          "https://github.com/evanq123/PushStocks \n")
    sys.exit(1)


api_key     = input("Enter your PushBullet api key: ")
symbol      = input("Enter the symbol: ").upper()
threshold   = float(input("Enter the amount in USD to start notifying: "))
intervals   = int(input("Enter the time (in seconds) between checks: "))


def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    html = requests.get(base_url + symbol).text
    soup = BeautifulSoup(html, "html.parser")
    quote = soup.find('span', attrs={'class': 'pr'}).text
    return quote


def push_message(msg, symbol):
    pb = PushBullet(api_key)
    pb.push_note("PushStocks: The quote for {} has changed!".format(symbol), msg)


message_sent = False # Hackish workaround for now.
def price_past_threshold():
    non_decimal = re.compile(r'[^\d.]+')
    quote = non_decimal.sub('', get_quote(symbol))
    if float(quote) >= float(threshold):
        return True


while True:
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if price_past_threshold() and message_sent is False:
        msg = ("As of, {} EST, the price for {} is >= {} USD (at {} USD)"
               "".format(date, symbol, threshold, get_quote(symbol).strip('\n')))
        print("Sending message to PushBullet...\n")
        push_message(msg, symbol)
        message_sent = True

    if not price_past_threshold() and message_sent is True:
        msg = ("As of, {} EST, the price for {} is < {} USD (at {} USD)"
               "".format(date, symbol, threshold, get_quote(symbol)))
        push_message(msg, symbol)
        message_sent = False

    time.sleep(intervals)
