"""Tests for `domicolor` module."""
from typing import Generator

import numpy as np
import pytest

import domicolor


@pytest.fixture
def version() -> Generator[str, None, None]:
    """Sample pytest fixture."""
    yield domicolor.__version__


def test_version(version: str) -> None:
    """Sample pytest test function with the pytest fixture as an argument."""
    assert version == "0.1.0"


def test_color_histogram(version: str) -> None:
    """Test color_histogram function."""
    image = np.zeros((10, 10, 3))
    hist = domicolor.color_histogram(image)
    true_hist = [0, 0, 0, 0, 0, 30000, 0, 0, 0, 0]
    assert np.alltrue(hist == true_hist)
