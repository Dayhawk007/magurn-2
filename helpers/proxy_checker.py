import requests


def scrape_proxies():
    api_url="https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=elite"
    proxies=requests.get(api_url).text.split("\n")
    return proxies

def check_and_get_proxies(proxies):
    for proxy in proxies[:100]:
        try:
            response = requests.get("https://www.google.com", proxies={"http": proxy.strip(), "https": proxy.strip()}, timeout=5)
            if response.status_code == 200:
                return proxy.strip()
        except Exception as e:
            pass
    





