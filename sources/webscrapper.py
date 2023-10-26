##
## EPITECH PROJECT, 2022
## Untitled (Workspace)
## File description:
## webscrapper
##

from urllib.request import urlopen
from bs4 import BeautifulSoup
import mechanicalsoup
import time
import sys

browser = mechanicalsoup.Browser()

def real_time_scrapper():
    for i in range(10):
        page = browser.get("http://olympus.realpython.org/dice")
        tag = page.soup.select("#result")[0]
        result = tag.text
        print(f"The result of your dice roll is: {result}")
        if i < 9:
            print("Rolling again...")
            time.sleep(2)

def mechanical_scrapper():
    url = "http://olympus.realpython.org/login"
    base_url = "http://olympus.realpython.org"
    login_page = browser.get(url)
    login_html = login_page.soup
    form = login_html.select("form")[0]
    form.select("input")[0]["value"] = "zeus"
    form.select("input")[1]["value"] = "ThunderDude"
    profiles_page = browser.submit(form, login_page.url)
    print(profiles_page.soup.title.text)
    if profiles_page.soup.title.text == "Log In":
        print("Login failed")
        return
    else:
        print("Login successful")
    print(profiles_page.url)
    links = profiles_page.soup.select("a")
    for link in links:
        address = link["href"]
        text = link.text
        print(f"{text}: {base_url}{address}")
    

def html_parser_exo1():
    url = "http://olympus.realpython.org/profiles"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a"):
        print(f"{'http://olympus.realpython.org'}{link.get('href')}")

def html_parser():
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    print(soup.get_text().replace("\n\n", "\n").strip())

def url_parser():
    url = "http://olympus.realpython.org/profiles/aphrodite"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)


def scraper(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return html

def webscrapper():
    if len(sys.argv) != 3:
        print("Usage: python3 webscrapper.py <url> <output_file>")
        return
    text = scraper(sys.argv[1])
    with open(sys.argv[2], "w") as f:
        f.write(text)