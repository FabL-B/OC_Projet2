from transform_package import transform
from load_package import load


def main():
    # Get the download path
    download_path = input("Enter the download path: ")

    # Get the book data dictionary as a list
    books_data_list = transform.get_books_info_dict()

    books_by_category = transform.sort_books_by_category(books_data_list)

    # Load book data into a CSV file sorted by categories
    load.load_data_csv(books_by_category, download_path)

    # Download book images with titles as filenames
    load.load_img(books_data_list, download_path)


if __name__ == "__main__":
    main()
