import os
import sys

import numpy as np
from PySide6.QtGui import QPixmap, QImage
from scipy.ndimage import gaussian_filter


# let's define our function for sharpening the image

def sharpen(image: np.ndarray, sigma: float = 1.0, amount: float = 1.0) -> np.ndarray:
    """
    Sharpen an image using an unsharp mask.

    Parameters
    ----------
    image : np.ndarray
        Input image (2D or 3D).
    sigma : float
        Standard deviation for Gaussian blur (larger = more smoothing).
    amount : float
        Strength of sharpening effect.

    Returns
    -------
    np.ndarray
        Sharpened image with the same shape as the input, returned as a float array.
    """

    # normalize to 0–1
    image = image / 255.0

    # Create a blurred version of the image
    blurred = gaussian_filter(image, sigma=sigma)

    # Isolating high-frequency detail (edges + fine detail)
    high_freq = image - blurred

    # add detail back to the original image
    sharpened = image + amount * high_freq

    # clip safely
    result = (np.clip(sharpened, 0, 1) * 255).astype(np.uint8)

    return result


def get_asset_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
