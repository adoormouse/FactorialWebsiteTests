
"""Unit Tests for Factorial Website 34.68.147.215:3389."""

import pytest
import requests
import math
import lxml.html

ip_address = "34.68.147.215"
port = "3389"
post_url = "factorial"
url = "http://{}:{}/{}".format(ip_address, port, post_url)
url_homepage = "http://{}:{}".format(ip_address, port)
page_title = "Factoriall"


def test_factorial_main_page():
    """Test for home page 200 response_code."""
    r = requests.post(url_homepage)
    assert r.status_code == 200


def test_factorial_title():
    """Test for home page title."""
    r = lxml.html.parse(url)
    assert page_title == r.find(".//title").text


def test_factorial_status_code_200():
    """Test statis_code 200, when posting data."""
    test_values = get_factorial_format(1)
    r = requests.post(url, data=test_values['data'])
    assert r.status_code == 200


def test_factorial_status_code_404():
    """Test for status_code 404, when using bad post url."""
    url_bad = "http://{}:{}/{}".format(ip_address, port, "bad")
    test_values = get_factorial_format(1)
    r = requests.post(url_bad, data=test_values['data'])
    assert r.status_code == 404


@pytest.mark.parametrize('number', range(1, 11, 1))
def test_factorial_int_positive_range(number):
    """Test for Positive Integer value."""
    test_values = get_factorial_format(number)
    r = requests.post(url, data=test_values['data'])

    answer = r.text
    assert answer == test_values['response']


def test_factorial_zero():
    """Test for Zero value."""
    test_values = get_factorial_format(0)
    r = requests.post(url, data=test_values['data'])

    answer = r.text
    assert answer == test_values['response']


def test_factorial_string():
    """Test for posting a string value."""
    test_values = get_factorial_format("hello world")
    r = requests.post(url, data=test_values['data'])

    status_code = r.status_code
    assert status_code == 400


def test_factorial_int_neg():
    """Test for Negative Integer value."""
    test_values = get_factorial_format(-6)
    r = requests.post(url, data=test_values['data'])

    status_code = r.status_code
    assert status_code == 400


def get_factorial_format(number):
    """Generate factorial and prvides formated values for testing."""
    try:
        if number >= 0:
            factorial = math.factorial(number)
            format_response = """{{\n  "answer": {}\n}}\n""".format(factorial)
            format_data = {'number': number}
            return {'data': format_data, 'response': format_response}
        else:
            format_response = "<class 'Value'>"
            format_data = {'number': number}
            return {'data': format_data, 'response': format_response}
    except:
        pass
        format_response = 400
        format_data = {'number': number}
        return {'data': format_data, 'response': format_response}
