# Books to Scrape ETL project

## Description :
Projet permettant d’extraire les données des 1000 livres du site http://books.toscrape.com et de télécharger leurs images.

## Fonctionnalités :
### Extract :
- Extrait tous les liens url des livres du site
- Extrait les données des livres depuis l’url du livre

### Transform :
- Classe les données de livre en dictionnaires
- Classe les livres par catégorie

### Load :
- Créer un fichier CSV pour chaque catégorie contenant les données des livres dans un dossier `Books_Data/`
- Télecharge toutes les images de livre dans un dossier `Pictures/`

## Installation :

1. Ouvrez Git Bash

    Remplacez le répertoire de travail actuel par l’emplacement où vous voulez mettre le répertoire cloné.

2. Cloner le dépôt sur votre machine locale:

    Clonez le dépôt
    ```bash
    git clone https://github.com/votre-utilisateur/votre-projet.git
    ```

3. Créer et activer l’environnement virtuel:
   
    ```bash
    Python -m venv env
    Source env/bin/activate (pour Linux et Mac)
    Env\Scripts\activate (pour Windows)```

4. Installer les packages:
   
    ```bash
    pip install -r requirements.txt
    ```

## Utilisation:
1. Executer le script principal
    ```bash
    python main.py
    ```
2. Entrer le chemin vers lequel seront téléchargée les images et les fichiers csv seront enregistrés
