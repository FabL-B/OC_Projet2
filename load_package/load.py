import requests
import os
import csv


# Function to write one csv file by category
# File name = category.csv
def load_data_csv(books_by_category, download_path):

    # Create path for folder where all csv files will be saved
    dl_path = os.path.join(download_path, "Books_Data")
    if not os.path.exists(dl_path):
        os.makedirs(dl_path)

    # Iterate over each category and its associated books
    for category, books in books_by_category.items():
        # Create a CSV file for each category
        file_path = os.path.join(dl_path, category + ".csv")
        with open(file_path, "w", newline="", encoding="utf-8") as csv_file:
            # Define the header for the CSV file
            fieldnames = [
                "product_page_url", "universal_product_code",
                "title", "price_including_tax", "price_excluding_tax",
                "number_available", "product_description", "category",
                "review_rating", "image_url"
            ]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            # Write each book's data to the CSV file
            for book in books:
                writer.writerow(book)
        print(f"{category}.csv containing {len(books)} books created")


# Function to download all images from books
# Image name = book_title.jpg
def load_img(books_data_list, download_path):
    # Create path for download folder
    dl_path = os.path.join(download_path, "Pictures")
    if not os.path.exists(dl_path):
        os.makedirs(dl_path)

    for book in books_data_list:
        # Get proper title as filename for pictures
        title = book["title"]
        forbid_chars = r'/\\:*?"<>|'
        for char in forbid_chars:
            title = title.replace(char, '-')

        img_url = book["image_url"]
        response = requests.get(img_url)

        # Download the image
        print("Downloading book pictures")
        print("...")
        file_path = os.path.join(dl_path, title + ".jpg")
        if os.path.exists(file_path):
            file_path = os.path.join(dl_path, title + "(1)" + ".jpg")
        with open(file_path, "wb") as f:
            f.write(response.content)
    print(f"{len(books_data_list)} images downloaded")
