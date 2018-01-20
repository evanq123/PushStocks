import sys
sys.path.insert(0, "lib")
import requests
import re
import time
from datetime import datetime

try:
    from bs4 import BeautifulSoup
    from pushbullet import PushBullet
except ImportError:
    print("Requirements were not installed. Please consult guide at\n"
          "https://github.com/evanq123/PushStocks \n")
    sys.exit(1)


api_key     = input("Enter your PushBullet api key: ")
symbol      = input("Enter the symbol: ")
threshold   = input("Enter the amount in USD to start notifying: ")
intervals   = int(input("Enter the time intervals (s) between checks: "))


def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    html = requests.get(base_url + symbol).text
    soup = BeautifulSoup(html, "html.parser")
    quote = soup.find('span', attrs={'class': 'pr'}).text
    return quote


def push_message(msg, symbol):
    pb = PushBullet(api_key)
    pb.push_note("PushStocks: The quote for {} has changed!".format(symbol), msg)


def send_message():
    non_decimal = re.compile(r'[^\d.]+')
    quote = non_decimal.sub('', get_quote(symbol))
    if float(quote) >= float(threshold):
        return True


while True:
    if send_message():
        msg = ("Price for {} went up to {} (threshold = {})\n"
               "".format(symbol, get_quote(symbol), threshold))
        print("Sending message to PushBullet...\n")
        push_message(msg, symbol)
    time.sleep(intervals)
