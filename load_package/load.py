import requests
import os

books_data_list = []

#fonction pour créer un fichier csv par catégorie
    #nom du fichier = nom_category.csv


#fonction pour télécharger les images de livres
    #nom d'image = titre_livre.jpg
def load_img():
    project_path = r"C:\Formation_OC\OC_Projet2" #?????
    dl_path = os.path.join(project_path, "downloads")
    print(dl_path)
    if not os.path.exists(dl_path):
        os.makedirs(dl_path)

    for book in books_data_list:    
        title = book["title"]
        img_url = book["image_url"]
        response = requests.get(img_url)

        file_path = os.path.join(dl_path, title + ".jpg")
        with open(file_path, "wb") as f:
            f.write(response.content)
        print("dl ok")
