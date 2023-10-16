import pytest
import requests
import re


@pytest.mark.http
def test_first_request():
    r = requests.get("https://football.ua/")
    assert r.status_code == 200



@pytest.mark.http
def test_second_request():
    r = requests.get("https://football.ua/profile/e6876641-422e-4aea-a282-66c47a22f8cf.html")
    body = r.content.decode()

    match = re.search(r'alt=\"yashanet\"', body)
    assert match is not None

@pytest.mark.http
def test_third_request():
    r = requests.get("https://football.ua/profile/e6876641-422e-4aea-a282-66c47a22f8cf.html")
    body = r.content.decode()

    match = re.search(r'alt=\"yashanet23\"', body)
    assert match is None



    #match = re.search(r"<title>(.*)</title>", body)
    #print(match)
    #if match:
        #print(match.group(1))
