import pytest
from selenium import webdriver
import time
import allure


@pytest.fixture
def browser():
    print('Browser open')
   
    options = webdriver.ChromeOptions()
    # options.add_argument('--incognito')
    # options.add_argument('--start-maximized')
    # options.add_argument('--disable-notifications')
    # докер
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    # time.sleep(10)
    print('Browser quit')
    driver.quit()  




# ХУК ДЛЯ СКРИНШОТОВ
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()


    if rep.failed:
        browser = item.funcargs.get("browser", None)


        if browser:
            allure.attach(
                browser.get_screenshot_as_png(),
                name=f"screenshot_{rep.when}",
                attachment_type=allure.attachment_type.PNG
            )
