import os

import pytest
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from source.lib import excel_automation as excel, constants
from source.lib.listeners import WebDriverListeners
from source.lib.selenium_actions import attach_screen_shot
from source.lib.webdriver_manager import create_driver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield 
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="session")
def set_environ():
    os.environ[constants.CHROME_VALUE] = constants.CHROME_PATH
    os.environ[constants.GECKO_VALUE] = constants.GECKO_PATH

@pytest.fixture(scope="function", params=["Chrome", "Chrome"], autouse=True)
def configuration(request):
    web_driver = None
    url = excel.get_cell_value(constants.EXCEL_PATH, "BrowserSetting", 0, "URL")
    if request.param =="Chrome":
        web_driver = create_driver("Chrome", url)
    elif request.param =="Chrome":
        web_driver = create_driver("Chrome", url)

    driver = EventFiringWebDriver(web_driver, WebDriverListeners())
    request.node.driver = driver
    yield
    if request.node.rep_call.failed:
        attach_screen_shot(driver, request.function.__name__)
    driver.close()
