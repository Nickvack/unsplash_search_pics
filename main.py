from custom_classes.saveimages import SaveImages
from custom_classes.getimages import  GetImages

# Data needed for the program to work
images_links = []
category = input('Category you want pictures from: ')
if ' ' in category:
    category.replace(" ", '-')

create_list = GetImages()
create_list.create_request(f'https://unsplash.com/s/photos/{category}')
create_list.pull_images_url(images_links)

save_images = SaveImages(f'{category}')
save_images.create_folder(f'{category}')
save_images.download_images(images_links[:9])