#!/usr/bin/python3
# -*- encoding=utf8 -*-

# This is example shows how we can manage failed tests
# and make screenshots after any failed test case.

import pytest

# import allure
import uuid


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def chrome_options(chrome_options):
    # chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1400,1000")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--log-level=DEBUG")

    return chrome_options


@pytest.fixture
def web_browser(request, selenium):
    browser = selenium

    # Return browser instance to test case:
    yield browser

    # Do teardown (this code will be executed after each test):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Make screen-shot for local debug:
            browser.save_screenshot(
                "screenshots/" + str(uuid.uuid4()) + ".png"
            )

            # Attach screenshot to Allure report:
            # allure.attach(
            #     browser.get_screenshot_as_png(),
            #     name=request.function.__name__,
            #     attachment_type=allure.attachment_type.PNG,
            # )

            # For happy debugging:
            print("URL: ", browser.current_url)
            print("Browser logs:")
            for log in browser.get_log("browser"):
                print(log)

        except Exception:
            pass  # just ignore any errors here
