import pytest
import requests
import re
from bs4 import BeautifulSoup



@pytest.mark.http
def test_website_response():
    r = requests.get("https://football.ua/")
    assert r.status_code == 200


@pytest.mark.http
def test_if_user_exist():
    r = requests.get("https://football.ua/profile/e6876641-422e-4aea-a282-66c47a22f8cf.html")
    body = r.content.decode()

    match = re.search(r'alt=\"yashanet\"', body)
    assert match is not None


@pytest.mark.http
def test_if_user_not_exist():
    r = requests.get("https://football.ua/profile/e6876641-422e-4aea-a282-66c47a22f8cf.html")
    body = r.content.decode()

    match = re.search(r'alt=\"yashanet23\"', body)
    assert match is None
