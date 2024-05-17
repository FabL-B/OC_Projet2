from extract_package import extract
from bs4 import BeautifulSoup
import requests
from pprint import pprint

main_url = "http://books.toscrape.com/"
home_page = requests.get(main_url)
home_soup = BeautifulSoup(home_page.text, "html.parser")


def get_books_links_in_list():
    category_link_list = extract.get_categories_links(home_soup)
    book_link_list = []
    for links in category_link_list:
        book_link = extract.get_books_links(links, links)
        book_link_list.extend(book_link)
    return book_link_list


def get_books_info_dict():
    book_link_list = get_books_links_in_list()
    books_data_list = []

    for book_link in book_link_list:
        book_page = requests.get(book_link)
        book_soup = BeautifulSoup(book_page.text, "html.parser")

        book_data_dict = {"product_page_url": book_link,
                          "universal_product_code": extract.get_upc(book_soup),
                          "title": extract.get_title(book_soup),
                          "price_including_tax": extract.get_price_incl_tax(book_soup),
                          "price_excluding_tax": extract.get_price_excl_tax(book_soup),
                          "number_available": extract.get_number_available(book_soup),
                          "product_description": extract.get_product_descr(book_soup),
                          "category": extract.get_category(book_soup),
                          "review_rating": extract.get_review_rating(book_soup),
                          "image_url": extract.get_image(book_soup)
                          }
        books_data_list.append(book_data_dict)
    return books_data_list


def sort_books_by_category(books_data_list):
    books_by_category = {}
    for book in books_data_list:
        category = book["category"]
        # check if category is already in books_by_category
        if category not in books_by_category:
            books_by_category[category] = []
        # add the book to the list of its category
        books_by_category[category].append(book)
    return books_by_category
