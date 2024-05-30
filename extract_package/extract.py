from bs4 import BeautifulSoup
import requests


main_url = "http://books.toscrape.com/"
home_page = requests.get(main_url)
home_soup = BeautifulSoup(home_page.text, "html.parser")


# Get all categories links in category_link_list
def get_categories_links(home_soup):
    category_link_list = []
    div_category = home_soup.find("div", class_="side_categories")
    li_category = div_category.find("li")
    ul_category = li_category.find("ul")
    a_category = ul_category.find_all("a")

    for a_href in a_category:
        link = main_url + a_href["href"]
        category_link_list.append(link)

    return category_link_list


# Get all books links from category_link_list
def get_books_links(raw_category_url, category_link):
    book_links = []

    raw_category_url = raw_category_url.replace("index.html", "")
    category_page = requests.get(category_link)
    category_soup = BeautifulSoup(category_page.text, "html.parser")

    h3s_category = category_soup.find_all("h3")

    # Find the book's URL
    for h3 in h3s_category:
        ahref_category = h3.find("a")
        book_link = (
            main_url + "catalogue/" + ahref_category["href"].strip("../../")
        )
        book_links.append(book_link)

    # Check if there is a next button
    next_button = category_soup.find("li", class_="next")
    if next_button:
        next_page = raw_category_url + next_button.find("a").get("href", "")
        # Recursively get the book links from the next page
        next_book_links = get_books_links(raw_category_url, next_page)
        book_links.extend(next_book_links)

    return book_links


# Extract universal product code (UPC)
def get_upc(book_soup):
    upc = book_soup.find_all("td")[0].text
    return upc


# Extract title
def get_title(book_soup):
    book_title = book_soup.find("h1").text
    return book_title


# Extract price including tax
def get_price_incl_tax(book_soup):
    price_including_tax = book_soup.find_all("td")[3].text
    return price_including_tax


# Extract price excluding tax
def get_price_excl_tax(book_soup):
    price_excluding_tax = book_soup.find_all("td")[2].text
    return price_excluding_tax


# Extract number avaiable
def get_number_available(book_soup):
    number_avaiable = book_soup.find_all("td")[5].text
    return number_avaiable


# Extract product description
def get_product_descr(book_soup):
    product_description = book_soup.find_all("p")[3].text
    return product_description


# Extract category
def get_category(book_soup):
    ul = book_soup.find("ul", class_="breadcrumb")
    category = ul.find_all("a")[2].text
    return category


# Extract review rating
def get_review_rating(book_soup):
    rating_class = book_soup.find("p", class_="star-rating").get("class")[1]
    review_rating = rating_class + " star"
    return review_rating


# Extract image URL :
def get_image(book_soup):
    img = book_soup.find("img").get("src").strip("../../")
    image_link = main_url + img
    return image_link
