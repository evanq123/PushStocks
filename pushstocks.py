import requests
import re
import sys
sys.path.insert(0, "lib")

try:
    from pushbullet import PushBullet
    from bs4 import BeautifulSoup
except ImportError:
    print("Requirements were not installed. Please consult guide at\n"
          "https://github.com/evanq123/PushStocks \n")
    sys.exit(1)


def get_quote(symbol):
    url = 'http://finance.yahoo.com/q?s={}'.format(symbol)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    print("Checking quotes for {}").format(symbol)
    data = soup.find('span', attrs={'id' : re.compile(r'yfs_.*?_{}'.format(symbol.lower()))})

    return data.text


def push_message(msg):
    try:
        pb = PushBullet(api_key)
        pb.push_note("PushStocks: Quotes have changed!", msg)
    except InvalidKeyError:
        print("An invalid API key was entered. Please consult guide at\n"
              "https://github.com/evanq123/PushStocks \n")

send_message = False
for symbol in symbols:
    quote = get_quote(symbol)
    msg = ''
    if float(quote) >= float(threshold):
        msg = msg + "Price for {} went up to {} "
                    "(threshold = {})\n".format(symbol, quote, threshold)
        send_message = True

    if send_message:
        print("Sending message to PushBullet...\n")
        push_message(msg)
