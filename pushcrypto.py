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


api_key     = input("Enter your PushBullet api key: ")
currency    = input("Enter the currency(full name): ").upper()
threshold   = float(input("Enter the amount in BTC to start notifying: "))
intervals   = int(input("Enter the time intervals (s) between checks: "))


def get_rate(currency): #This works, but is very slow
    currency = currency.replace(" ", "-")
    base_url = 'http://coinmarketcap.com/currencies/'
    url = urlopen(base_url + currency + "/")
    soup = BeautifulSoup(url, "html.parser")
    rate = soup.find('span', attrs={"class": "text-gray details-text-medium"}).text
    return rate


def push_message(msg, symbol):
    pb = PushBullet(api_key)
    pb.push_note("PushStocks: The rate for {} has changed!".format(symbol), msg)


message_sent = False # Hackish workaround for now.
def price_past_threshold():
    non_decimal = re.compile(r'[^\d.]+')
    quote = non_decimal.sub('', get_quote(currency))
    if float(quote) >= float(threshold):
        return True


while True:
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if price_past_threshold() and message_sent is False:
        msg = ("As of, {} EST, the rate for {} is >= {} BTC (at {} BTC)"
               "".format(date, currency, threshold, get_quote(currency)))
        print("Sending message to PushBullet...\n")
        push_message(msg, currency)
        message_sent = True

    if not price_past_threshold() and message_sent is True:
        msg = ("As of, {} EST, the rate for {} is < {} BTC (at {} BTC)"
               "".format(date, currency, threshold, get_quote(currency)))
        print("Sending message to PushBullet...\n")
        push_message(msg, currency)
        message_sent = False

    time.sleep(intervals)
