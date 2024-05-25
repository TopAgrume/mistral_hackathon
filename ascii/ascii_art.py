from rembg import remove
import numpy as np
from PIL import Image
import argparse

DEFAULT_ASCII_CHARS = '@%#*+=-:. '
DEFAULT_ASCII_CHARS2 = '@#|\\/-_.: '

def resize_image(image, new_width=100):
    """Resize the image while maintaining aspect ratio."""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width * 2, new_height))

def grayscale_image(image):
    """Convert the image to grayscale."""
    return image.convert('L')

def image_to_ascii(image, ascii_chars=DEFAULT_ASCII_CHARS):
    """Convert the image to ASCII art."""
    image = grayscale_image(image)
    pixels = np.array(image)

    pixel_range = len(ascii_chars) - 1
    ascii_str = '\n'.join(
        ''.join(ascii_chars[pixel_value * pixel_range // 255] for pixel_value in row)
        for row in pixels
    )

    return ascii_str

def load_image(input_image_path):
    """Load an image from the specified path."""
    try:
        image = Image.open(input_image_path)
        image = remove(image)
        return image
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The specified image file '{input_image_path}' was not found.")
    except Exception as e:
        raise Exception(f"Error: Failed to load image '{input_image_path}': {e}")

def validate_output_width(output_width):
    """Validate the output width argument."""
    if not isinstance(output_width, int) or output_width <= 0:
        raise ValueError("Error: Output width must be a positive integer.")

def generate_ascii_art(image, output_width=100, ascii_chars=DEFAULT_ASCII_CHARS):
    """Generate ASCII art from an image."""
    validate_output_width(output_width)
    image = resize_image(image, output_width)
    ascii_art = image_to_ascii(image, ascii_chars)
    return ascii_art

def save_ascii_art_to_file(ascii_art, output_file):
    """Save the ASCII art to a text file."""
    try:
        with open(output_file, 'w') as file:
            file.write(ascii_art)
        print(f"ASCII art saved to '{output_file}'.")
    except Exception as e:
        raise Exception(f"Error: Failed to save ASCII art to '{output_file}': {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate ASCII art from an image.")
    parser.add_argument("input_image_path", type=str, help="Path to the input image.")
    parser.add_argument("--output_width", type=int, default=32, help="Width of the output ASCII art.")
    parser.add_argument("--ascii_chars", type=str, default=DEFAULT_ASCII_CHARS, help="Custom ASCII characters for the art.")
    parser.add_argument("--output_file", type=str, help="Path to save the ASCII art as a text file.")
    args = parser.parse_args()

    input_image_path = args.input_image_path
    output_width = args.output_width
    ascii_chars = args.ascii_chars
    output_file = args.output_file

    input_image = load_image(input_image_path)
    
    ascii_art = generate_ascii_art(input_image, output_width, ascii_chars)

    if output_file:
        save_ascii_art_to_file(ascii_art, output_file)
    else:
        print(ascii_art)
