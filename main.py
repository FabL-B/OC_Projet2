from transform_package import transform
from load_package import load


def main():

    # Get the book data dictionnary in list
    books_data_list = transform.get_books_info_dict()

    # Load books data in CSV file sorted by categories
    load.load_data_csv(books_data_list)

    # Download books pictures with title as filename
    load.load_img(books_data_list)


if __name__ == "__main__":
    main()
