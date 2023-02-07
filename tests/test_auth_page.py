import pickle

from pages.auth_page import AuthPage


def test_auth_valid_email_pass(web_browser):
    page = AuthPage(web_browser)

    page.email.send_keys("xalax48121@xegge.com")

    page.password.send_keys("KivAknZcs5yep")

    page.btn.click()

    # # Save cookies
    # with open("cookies.txt", "wb") as cookies:
    #     pickle.dump(web_browser.get_cookies(), cookies)

    expected_url = "https://petfriends.skillfactory.ru/all_pets"

    assert page.get_current_url() == expected_url


def test_auth_valid_cookie(web_browser):
    page = AuthPage(web_browser, url="https://petfriends.skillfactory.ru")

    with open("cookies.txt", "rb") as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            web_browser.add_cookie(cookie)
        web_browser.refresh()

    expected_url = "https://petfriends.skillfactory.ru/all_pets"

    assert page.get_current_url() == expected_url
