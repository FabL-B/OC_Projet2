# Books to Scrape ETL project

## Description :
Project allowing to extract data from the 1000 books on the website http://books.toscrape.com and to download their images.

## Features :
### Extract :
- Extracts all book URL links from the site.
- Extracts book data from the book URL.

### Transform :
- Converts book data into dictionaries.
- Organizes books by category.

### Load :
- Creates a CSV file for each category containing book data in a `Books_Data/` directory.
- Downloads all book images into a `Pictures/` directory.

## Installation :

1. Open Git Bash

    Change the current working directory to the location where you want the cloned directory to be.

2. Clone the repository to your local machine:

    Clone the repository.
    ```bash
    git clone https://github.com/votre-utilisateur/votre-projet.git
    ```

3. Create and activate the virtual environment:
   
    ```bash
    Python -m venv env
    Source env/bin/activate (pour Linux et Mac)
    Env\Scripts\activate (pour Windows)```

4. Install the packages:
   
    ```bash
    pip install -r requirements.txt
    ```

## Usage:
1. Run the main script.
    ```bash
    python main.py
    ```
2. Enter the path where the images will be downloaded and the CSV files will be saved.

3. For demo purpose, we can modify the `get_categories_links` function in `extract.py` to return only the first 3 categories from the list.

    ```python
    return category_link_list
    ```
    to:

    ```python
    return category_link_list[:3]
    ```
