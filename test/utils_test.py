import pytest
import hashlib
from src.utils import generate_hash


@pytest.fixture
def test_url():
    return "www.google.com"


def test_generate_hash(test_url):
    expect_result = hashlib.sha256(test_url.encode("utf-8")).hexdigest()
    assert expect_result + "sad" == generate_hash(test_url)
