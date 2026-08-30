from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image, print its shape and return the pixel array in RGB.
    """
    try:
        img = Image.open(path)
        img = img.convert("RGB")
        array = np.array(img)

        print(f"The shape of image is: {array.shape}")
        return array

    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None