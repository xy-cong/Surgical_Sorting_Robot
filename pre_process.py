import numpy as np
from PIL import Image
import os

def load_images_from_folder(folder):
    default_size = (4096, 3072)
    images = []
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder,filename))
        if img is not None:
            if img.size[0] < img.size[1]:
                img = img.rotate(90, expand=True)
            images.append(img)
        assert img.size == default_size, "Image size is not 4096x3072"
    return images, default_size

def resize_images(images, size):
    resized_images = []
    for img in images:
        img = img.resize(size)
        resized_images.append(img)
    return resized_images

def resize_images_by_factor(images, factor):
    resized_images = []
    for img in images:
        img = img.resize((int(img.size[0] * factor), int(img.size[1] * factor)))
        resized_images.append(img)
    return resized_images

def convert_images_to_array(images):
    images_array = []
    for img in images:
        img = np.array(img)
        images_array.append(img)
    return images_array

def save_images_to_folder(images, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    for i in range(len(images)):
        img = Image.fromarray(images[i])
        img.save(folder + f'{i:04d}.png')

def resize_and_save():
    folder = 'photos/oh'
    images, _ = load_images_from_folder(folder)
    resize_factor = 0.25
    resized_images = resize_images_by_factor(images, resize_factor)
    images_array = convert_images_to_array(resized_images)
    save_images_to_folder(images_array, 'resized_data/')
    print("Done")

if __name__ == "__main__":
    resize_and_save()
    