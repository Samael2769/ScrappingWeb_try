##
## EPITECH PROJECT, 2022
## Untitled (Workspace)
## File description:
## webscrapper
##

from urllib.request import urlopen
from bs4 import BeautifulSoup

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

def webscrapper():
    #url_parser()
    #html_parser()
    html_parser_exo1()