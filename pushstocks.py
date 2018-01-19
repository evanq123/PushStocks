import sys
sys.path.insert(0, "lib")
import requests

try:
    from bs4 import BeautifulSoup
    from pushbullet import PushBullet
except ImportError:
    print("Requirements were not installed. Please consult guide at\n"
          "https://github.com/evanq123/PushStocks \n")
    sys.exit(1)


def get_quote(symbol):
    base_url = 'http://finance.google.com/finance?q='
    html = requests.get(base_url + symbol).text
    soup = BeautifulSoup(html, "html.parser")
    quote = soup.find('span', attrs={'class': 'pr'}).text
    return quote


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
