import urllib.request
import os
import pathlib


class SaveImages:
    def __init__(self, category):
        self.current_path = pathlib.Path().resolve()
        self.img_directory = os.path.join(self.current_path, category)

    def create_folder(self, category):

        if not os.path.exists(category):
            os.mkdir(self.img_directory)

    def download_images(self, images_links):
        x = 1
        for link in images_links:

            urllib.request.urlretrieve(link, f'{os.path.join(self.img_directory, str(x))}.png')
            x += 1
