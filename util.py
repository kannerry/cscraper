import requests
import os
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}

def soup_grab_html(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        rendered_html = response.text
        soup = BeautifulSoup(rendered_html, "html.parser")
        return soup
    else:
        print("Failed to retrieve the webpage.")
        print(response)
        return 0

def grab_site_main(url):
    site_split_pre = str(url).split("://")
    if not site_split_pre.__len__() == 1:
        site_split_post = site_split_pre[1].split("/")
        return site_split_post[0]
    else:
        return "ret"

def grab_scripts(dir):
    i = 0
    print("")
    print("-- scripts --")
    for filename in os.listdir(dir):
        if filename.endswith(".py"):
            i += 1
            print(i, ":", filename)
    print("-------------")
    retval = os.listdir(dir)
    retval.pop()
    return retval