from pages.base import WebPage
import os

from pages.elements import WebElement


class AuthPage(WebPage):
    def __init__(self, web_driver, url=""):
        if not url:
            url = (
                os.getenv("MAIN_URL")
                or "https://petfriends.skillfactory.ru/login"
            )

        super().__init__(web_driver, url)

    email = WebElement(id="email")

    password = WebElement(id="pass")

    btn = WebElement(class_name="btn.btn-success")
