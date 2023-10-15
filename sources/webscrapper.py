##
## EPITECH PROJECT, 2022
## Untitled (Workspace)
## File description:
## webscrapper
##

from urllib.request import urlopen

def webscrapper():
    url = "http://olympus.realpython.org/profiles/aphrodite"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)