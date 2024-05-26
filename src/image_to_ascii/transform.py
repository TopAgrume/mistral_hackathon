# %%
import os
import csv
import cv2
from PIL import Image
from tqdm import tqdm
import numpy as np
from rembg import remove as remove_background


DEFAULT_ASCII_CHARS = ' .:-=+*#%@'

# %%
def resize_image(image, new_width=60):
    """Resize the image while maintaining aspect ratio."""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width * 2, new_height))

def grayscale_image(image):
    """Convert the image to grayscale."""
    return image.convert('L')

"""def pixels_to_ascii(image):
    pixels = image.getdata()
    duplicated_pixels = [pixel for pixel in pixels for _ in range(2)]
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in duplicated_pixels])
    return characters"""

def sentencify(ascii_art_list: list, new_width):
    pixel_count = len(ascii_art_list) * 2
    ascii_image = "\n".join([ascii_art_list[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    return ascii_image

def image_to_ascii(image, ascii_chars=DEFAULT_ASCII_CHARS, size=40):
    """Convert the image to ASCII art."""
    pixels = image.getdata()
    pixel_range = len(ascii_chars) - 1
    characters = "".join([ascii_chars[pixel_value * pixel_range // 255]for pixel_value in pixels])
    return sentencify(characters, size)

def csv_save(file_name, data):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# %%
def load_image(input_image_path, no_pg_process):
    """Load an image from the specified path."""
    image = Image.open(input_image_path)
    if not no_pg_process:
        image = remove_background(image)

    image = grayscale_image(image)

    image_csv2 = np.array(image)
    mask = image_csv2 > 10
    image_csv2 = image_csv2[np.ix_(mask.any(1), mask.any(0))]

    pil_image = Image.fromarray(image_csv2)
    return pil_image

# %%
def generate_ascii_art(image, output_width, ascii_chars=DEFAULT_ASCII_CHARS):
    """Generate ASCII art from an image."""
    image = resize_image(image, output_width)
    ascii_art = image_to_ascii(image, ascii_chars, output_width*2)
    return ascii_art

# %%
ascii_chars = ' .:-=+*#%@'

def main(data_path, csv_ascii_30_path, csv_asccii_60_path):
    for datasets_name in os.listdir(data_path):
        dataset_path = os.path.join(data_path, datasets_name)

        for class_ in os.listdir(dataset_path):
            class_path = os.path.join(dataset_path, class_)
            ascii_30, ascii_60 = [], []
            i = 0
            for sample in tqdm(os.listdir(class_path)):
                sample_path = os.path.join(class_path, sample)
                #print(f"Processing: Dataset {datasets_name}, Class {class_}, Sample {sample}")
                input_image = load_image(sample_path, "no_bg" in sample_path)

                ascii_30.append([generate_ascii_art(input_image, 25, ascii_chars), class_, sample])
                ascii_60.append([generate_ascii_art(input_image, 40, ascii_chars), class_, sample])

                if i == 5:
                    break
                i += 1
            csv_save(os.path.join(csv_ascii_30_path, f"ascii_30_{datasets_name}dd_{class_}.csv"), ascii_30)
            csv_save(os.path.join(csv_asccii_60_path, f"ascii_60_{datasets_name}dd_{class_}.csv"), ascii_60)
            return
    print('===> Done <===')

# %%
data_path = os.path.join(os.getcwd(), "src", "image_to_ascii", "data")
data_path

# %%
ascii_30_path = os.path.join(os.getcwd(),  "src", "image_to_ascii", "ascii_30")
ascii_30_path

# %%
ascii_60_path = os.path.join(os.getcwd(),  "src", "image_to_ascii", "ascii_60")
ascii_60_path

# %%
if __name__ == "__main__":
    main(data_path, ascii_30_path, ascii_60_path)