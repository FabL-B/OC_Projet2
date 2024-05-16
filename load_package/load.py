import requests
import os
import csv


# fonction pour créer un fichier csv par catégorie
# nom du fichier = nom_category.csv
def load_data_csv(books_data_list):
    # Create the folder Books_Data where all csv files will be saved
    project_path = r"C:\Formation_Dev_Python_OC\Projet_2"
    dl_path = os.path.join(project_path, "Books_Data")
    if not os.path.exists(dl_path):
        os.makedirs(dl_path)

    for book in books_data_list:
        # csv files will have the name of the value from the key "category"
        category = book["category"]
        file_path = os.path.join(dl_path, category + ".csv")
        # create the csv file with header
        with open(file_path, "w", newline="", encoding="utf-8") as csv_file:
            fieldnames = [
                "product_page_url", "universal_product_code", "title",
                "price_including_tax", "price_excludind_tax", "number_avaible",
                "product_description", "category", "review_rating", "image_url"
            ]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            # iterate in books_data_list to write the data in csv file
            for book_data in books_data_list:
                writer.writerow(book_data)


# fonction pour télécharger les images de livres
# nom d'image = titre_livre.jpg
def load_img(books_data_list):

    # create path for download folder
    project_path = r"C:\Formation_Dev_Python_OC\Projet_2"
    dl_path = os.path.join(project_path, "Pictures")
    if not os.path.exists(dl_path):
        os.makedirs(dl_path)

    for book in books_data_list:
        # get proper title as filename for pictures
        title = book["title"]
        forbid_chars = r'/\\:*?"<>|'
        for char in forbid_chars:
            title = title.replace(char, '-')

        img_url = book["image_url"]
        response = requests.get(img_url)

        # download the image
        file_path = os.path.join(dl_path, title + ".jpg")
        with open(file_path, "wb") as f:
            f.write(response.content)
