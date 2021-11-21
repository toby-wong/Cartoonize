from utils import *
from os import path,listdir
import requests, shutil, sys
"""
Cartoonize Photo API
    Toby Wong
"""


def upload_image(path_to_image):
    """
    POST: Uploads an image to the server.

    images = {'image': open(path_to_image, 'rb')}
    output = requests.post(server, files=images)
    return output.text
    """

    # "upload" (copy) image to "server"
    shutil.copy('./local/' + path_to_image, './library')
    print(path.basename(path_to_image) + ' uploaded to server.')
    return path.exists('./library/' + path.basename(path_to_image))

def download_image(image_name, cartoon=True):
    """
    GET: Downloads an image from the server.

    if cartoon:
        image = Cartooner(image_name)
        image.save_cartoon()
        image_name = image.new_filename
    output = requests.get(server + image_name)
    with open(image_name, 'wb') as file:
        file.write(local_directory + image_name)
    return path.exists(local_directory + image_name)
    """

    if not path.exists('./library/' + image_name):
        print('Image does not exist on server.')
        return False

    # "download" (copy) image from "server"
    if cartoon:
        image = Cartooner('./library/' + image_name)
        image.save_cartoon(directory='./library/')
        image_name = image.new_filename
    shutil.copy('./library/' + image_name, './local/')
    return path.exists('./library/' + image_name)

def list_images():
    """
    GET: Lists all images on the server.

    output = requests.get(server)
    return output.text
    """

    # list all images on "server"
    return [filename for filename in listdir('./library')]


if __name__ == "__main__":
    
    # initialise cartoonize
    if len(sys.argv) != 1:
        print("Usage: python cartoonize_api.py")
        sys.exit(1)

    print("Initialising Cartoonize")
    # start server/user login implementation

    print("Welcome to Cartoonize")

    while True:
        print("\nWhat would you like to do?")
        print("1. Upload an image")
        print("2. Download an image")
        print("3. List all images")
        print("4. Exit")
        choice = input("Enter your choice: ")

        # upload image
        if choice == "1":
            print("Upload an image")
            image_name = input("Enter the name of the image: ")
            if path.exists('./local/'+image_name) and upload_image(image_name):
                print("Image uploaded successfully")
            else:
                print("Image upload failed")

        # download image
        elif choice == "2":
            print("Download an image")
            image_name = input("Enter the name of the image: ")
            cartoon = input("Cartoon? (y/n): ")
            if download_image(image_name, cartoon == "y"):
                print("Image downloaded successfully")
            else:
                print("Image download failed")
        
        # list images
        elif choice == "3":
            print("List all images")
            print(list_images())

        # exit
        elif choice == "4":
            print("Exiting Cartoonize")
            sys.exit(0)

        else:
            print("Invalid choice")