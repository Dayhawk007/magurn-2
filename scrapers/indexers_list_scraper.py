import requests
from bs4 import BeautifulSoup
import sys

sys.path.insert(0,"E:\\Development\\magurn-2\\helpers\\")

from proxy_checker import scrape_proxies,check_and_get_proxies



def scrape_indexers():
    print("Scraping indexers from megathread......")
    
    megathread_url="https://www.reddit.com/r/Piracy/wiki/megathread/all_purpose/"
    
    proxy=check_and_get_proxies(scrape_proxies())
    
    indexers_list=[]
    
    with requests.session() as r:
        r.headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
            "Referer": "https://www.reddit.com/r/Piracy/wiki/megathread/"
        }
        
        r.proxies={
            "http": proxy.strip(), "https": proxy.strip()
        }
        
        megathread_html=r.get(megathread_url).text
        
        soup=BeautifulSoup(megathread_html,features="html.parser")
        
        startIndex=999999999
        endIndex=9999999999
        for index,listItem in enumerate(soup.find_all("h3")):
            if("1337x" in listItem.text):
                startIndex=index
            
            if(index>=startIndex):
                all_links=listItem.find_all("a")
                for link in all_links:
                    print(link)
                    indexers_list.append(link["href"])
            
            if("TorrentLeech" in listItem.text):
                endIndex=index
            
            if(index>=endIndex):
                break                
    return indexers_list

scrape_indexers()