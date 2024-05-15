from extract_package import extract
from bs4 import BeautifulSoup
import requests

main_url = "http://books.toscrape.com/"
home_page = requests.get(main_url)
home_soup = BeautifulSoup(home_page.text, "html.parser")


def get_books_links_in_list():
    category_link_liste = extract.get_categories_links(home_soup)
    book_link_liste = []
    for links in category_link_liste:
        book_link = extract.get_books_links(links, links)
        book_link_liste.extend(book_link)
    return book_link_liste



