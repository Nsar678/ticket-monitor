import requests

URL = "https://shop.weeztix.com/6c90b596-eac7-4f34-b20e-eb43350a7c40/tickets"
KEYWORD = "Keine Tickets verfügbar"

def check():
    r = requests.get(URL, timeout=10)
    return KEYWORD not in r.text

if check():
    print("TICKETS VERFÜGBAR")
else:
    print("noch nichts")
