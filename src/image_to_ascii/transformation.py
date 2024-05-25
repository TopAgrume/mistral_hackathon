import PIL
import os

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

def resize_image(image, new_width=20):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height)) # TODO copy
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)


def main(directory_path, new_width=100):
    for datasets_name in os.listdir(directory_path):
        dataset_path = os.path.join(directory_path, datasets_name)

        for class_ in os.listdir(dataset_path):
            class_path = os.path.join(dataset_path, class_)

            for sample in os.listdir(class_path):
                sample_path = os.path.join(class_path, sample)
                try:
                    image = PIL.Image.open(sample_path)
                    ascii_20 = grayify(resize_image(image.copy()))

                except:
                    print(sample_path, " is not a valid pathname to an image.")


    # convert image to ascii
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    # format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    # print result
    print(ascii_image)

    # save result to "ascii_image.txt"
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)





if __name__ == '__main__':
    data_path = ""
    main()