"""Main module."""
import numpy as np


def color_histogram(image: np.ndarray) -> np.ndarray:
    """Color histogram function.

    Args:
        image: lll

    Returns:
        histogram of the image
    """
    return np.histogram(image)[0]
