from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure
from source.lib.selenium_actions import click

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        
    __logout_button = (By.ID, "logoutLink")
    
    @allure.step
    def click_on_logout(self):
        click(self.find_element(*self.__logout_button))
     
    @allure.step   
    def verify_title(self, title):
        flag = False
        wait = WebDriverWait(self.driver, 30)
        try:
            flag = wait.until(ec.title_contains(title), 
                              "Verifying the title: "+title)
            return flag
        except TimeoutException:
            print("Title is not loaded: ",title)
            return flag

    def find_element(self, By, attribute_value):
        web_element = None
        try:
            web_element = self.driver.find_element(By, attribute_value)
        except NoSuchElementException:
            print("Unable to find the web element", NoSuchElementException)
        
        return web_element