# %%
import PIL
import os
import csv
from PIL import Image
from tqdm import tqdm
from rembg import remove as remove_background
from multiprocessing import Pool

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# %%
def resize_image(image, new_width=20):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height)) # TODO copy
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    duplicated_pixels = [pixel for pixel in pixels for _ in range(2)]
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in duplicated_pixels])
    return characters

def sentencify(ascii_art_list: list, new_width):
    pixel_count = len(ascii_art_list) * 2
    ascii_image = "\n".join([ascii_art_list[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    return ascii_image

def csv_save(file_name, data):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def process_image(sample_path):
    try:
        image = Image.open(sample_path)
        image = remove_background(image)
        image_grey_20 = grayify(resize_image(image.copy(), 20))
        image_grey_100 = grayify(resize_image(image.copy(), 100))
        ascii_20 = sentencify(pixels_to_ascii(image_grey_20), 40)
        ascii_100 = sentencify(pixels_to_ascii(image_grey_100), 200)
        return ascii_20, ascii_100
    except Exception as e:
        print(sample_path, " is not a valid pathname to an image.")
        return None, None

def main(data_path, csv_ascii_20_path, csv_asccii_100_path):
    ascii_20, ascii_100 = [], []
    pool = Pool()
    for datasets_name in os.listdir(data_path):
        dataset_path = os.path.join(data_path, datasets_name)
        for class_ in os.listdir(dataset_path):
            class_path = os.path.join(dataset_path, class_)
            sample_paths = [os.path.join(class_path, sample) for sample in os.listdir(class_path)]
            results = list(tqdm(pool.imap(process_image, sample_paths), total=len(sample_paths)))
            for result, sample_path in zip(results, sample_paths):
                if result[0] is not None:
                    ascii_20.append([result[0], class_, os.path.basename(sample_path)])
                if result[1] is not None:
                    ascii_100.append([result[1], class_, os.path.basename(sample_path)])

    csv_save(csv_ascii_20_path, ascii_20)
    csv_save(csv_asccii_100_path, ascii_100)
    print('===> Done <===')

# %%
data_path = os.path.join(os.getcwd(), "data")
data_path

# %%
ascii_20_path = os.path.join(os.getcwd(), "ascii_20", "ascii_20.csv")
ascii_20_path

# %%
ascii_100_path = os.path.join(os.getcwd(), "ascii_100", "ascii_100.csv")
ascii_100_path

# %%
main(data_path, ascii_20_path, ascii_100_path)

# %%
import pandas as pd

df_ascii_20 = pd.read_csv(ascii_20_path, header=None, names=["ascii_art", "class", "sample_name"])
df_ascii_100 = pd.read_csv(ascii_100_path, header=None, names=["ascii_art", "class", "sample_name"])


# %%
df_ascii_20

# %%


# %%



