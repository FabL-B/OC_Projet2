from extract_package import extract
from bs4 import BeautifulSoup
import requests


main_url = "http://books.toscrape.com/"
home_page = requests.get(main_url)
home_soup = BeautifulSoup(home_page.text, "html.parser")


# Get all the books url links in a list
def get_books_links_in_list():
    category_link_list = extract.get_categories_links(home_soup)
    book_link_list = []
    for links in category_link_list:
        book_link = extract.get_books_links(links, links)
        book_link_list.extend(book_link)
    return book_link_list


# Get all books datas from extract package in dictionnaries
def get_books_info_dict():
    book_link_list = get_books_links_in_list()
    books_data_list = []

    for book_link in book_link_list:
        book_page = requests.get(book_link)
        book_soup = BeautifulSoup(book_page.text, "html.parser")

        book_data_dict = {
            "product_page_url": book_link,
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
    print("books datas in dictionnaries")
    return books_data_list


# Sort books by category with category as a key and book list as value
def sort_books_by_category(books_data_list):
    books_by_category = {}
    for book in books_data_list:
        category = book["category"]
        # Check if category is already in books_by_category
        if category not in books_by_category:
            books_by_category[category] = []
        # Add the book to the list of its category
        books_by_category[category].append(book)
    print("books dictionnaries sorted by category")
    return books_by_category
