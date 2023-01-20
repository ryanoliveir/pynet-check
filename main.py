import requests as req
from requests.exceptions import ConnectTimeout

TIMEOUT  = 3
site_address = "www.google.com"

def checkConnection(url):
    try:
        req.get('https://' + url, timeout=TIMEOUT)
        return True
    except ConnectTimeout:
        return False


if __name__ == "__main__":

    checkConnection(site_address)

    status = "Access internet!" if checkConnection(site_address) else "No internet connection!"

    print(status)
    
