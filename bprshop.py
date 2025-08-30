import requests
import re

def get_price(url):
    response = requests.get(url)
    match = re.search(r'data-value="(\d+)"', response.text)
    if match:
        return int(match.group(1)) 
    else:
        return None

url = "https://www.bprshop.com/product/12673-Asus-G815LW-Ultra9-32-2-12"
price = get_price(url)
print(price)

