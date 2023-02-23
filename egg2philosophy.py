import requests
from bs4 import BeautifulSoup
import time

URL = "https://en.wikipedia.org/wiki/Egg"
n = 100

URL = input('start URL : ')

def is_link_valid(new_link,old_link):
    '''1. Clicking on the first non-parenthesized, non-italicized link
    2. Ignoring external links, links to the current page, or red links (links to non-existent pages)
    3. Stopping when reaching "Philosophy", a page with no links or a page that does not exist, or when a loop occurs
    '''
    forbidden_signs = '[]{}()'
    for symbol in forbidden_signs:
        if symbol in new_link.text:
            # print(new_link)
            # time.sleep(3)
            return False
    
    rule2_fail = False
    href = new_link['href']

    if href.startswith('#'):
        rule2_fail = True

    if 'wikipedia.org' not in href:
        if not href.startswith('/'):
            rule2_fail = True

    if rule2_fail:
        # print(new_link)
        # time.sleep(3)
        return False

    return True

    


for i in range(n):
    r = requests.get(URL, "html.parser")

    soup = BeautifulSoup(r.content)
    print(f'({i}){soup.title.text} => {URL}')
    if 'philosophy' in soup.title.text.lower():
    # if URL == "https://en.wikipedia.org/wiki/Philosophy":
        print(f'*****reached the goal with {i} steps*****')
        break
    baseURL = 'https://en.wikipedia.org'

    body = soup.find(id="mw-content-text")
    paras = body.find_all('p')
    # links = [elem['href'] for elem in paras[0].find_all('a', href=True)]

    #get new url
    got_new_link = False
    for p in paras:
        if got_new_link:
            break
        for new_URL in p.find_all('a', href=True):
            if is_link_valid(new_URL, URL):

                new_URL = new_URL['href']
                if new_URL.startswith('/'):
                    new_URL = baseURL + new_URL

                URL = new_URL
                got_new_link = True
                break
