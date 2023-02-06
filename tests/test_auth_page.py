# import pytest
from pages.auth_page import AuthPage


def test_authorisation(web_browser):
    page = AuthPage(web_browser)

    page.email.send_keys("xalax48121@xegge.com")

    page.password.send_keys("KivAknZcs5yep")

    page.btn.click()

    expected_url = "https://petfriends.skillfactory.ru/all_pets"

    assert page.get_current_url() == expected_url
