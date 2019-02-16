import allure
from selenium.webdriver.common.by import By

from source.lib.selenium_actions import send_keys, click, text
from source.pages.base_page import BasePage


class LoginPage(BasePage):
    
    __username = (By.ID, "username")
    __password = (By.NAME, "pwd")
    __loginButton = (By.ID, "loginButton")
    __error_message = (By.XPATH, "//span[@class='errormsg' and not(@id)]")
    
    @allure.step
    def enter_username(self, user_name):
        send_keys(self.find_element(*self.__username), user_name)
        
    @allure.step
    def enter_password(self, password):
        send_keys(self.find_element(*self.__password), password)
    
    @allure.step
    def click_login_button(self):
        click(self.find_element(*self.__loginButton))

    @allure.step
    def get_error_message(self):
        error_value = text(self.find_element(*self.__error_message))
        return error_value