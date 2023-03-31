from django.test import Client
from django.urls import reverse


# testing that pytest works
def test_addition():
    assert 2 + 2 == 4


# testing that pytest works (by giving a fail)
def test_addition():
    assert 2 + 2 == 6


# testing that the template can be accesed
def test_my_template():
    client = Client()

    # Make a GET request to the view that renders the template
    response = client.get(reverse('home'))

    # Check that the response contains the expected content
    expected_content = 'Welcome to BookBot!'
    assert expected_content in str(response.content)
