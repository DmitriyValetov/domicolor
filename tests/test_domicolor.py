"""Tests for `domicolor` module."""
from typing import Generator

import numpy as np
import pytest

import domicolor
from domicolor.domicolor import color_histogram


@pytest.fixture
def version() -> Generator[str, None, None]:
    """Sample pytest fixture."""
    yield domicolor.__version__


def test_version(version: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert version == "0.1.1"


def test_color_histogram() -> None:
    """Test color_histogram function."""
    image = np.zeros((100, 100, 3))
    hist = color_histogram(image)
    true_hist = [0, 0, 0, 0, 0, 30000, 0, 0, 0, 0]
    assert np.all(hist == true_hist)
