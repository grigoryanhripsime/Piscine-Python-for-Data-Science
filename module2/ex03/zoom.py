from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    try:
        img = ft_load("animal.jpeg")
        if img is None:
            return

        print(img)

        zoomed = img[100:500, 450:850]

        zoomed = zoomed[:, :, 0]

        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        plt.imshow(zoomed, cmap="gray")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()