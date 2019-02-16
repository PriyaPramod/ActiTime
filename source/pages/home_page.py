from selenium.webdriver.common.by import By

from source.lib.selenium_actions import click, text
from source.pages.base_page import BasePage


class HomePage(BasePage):
    
    __help_menu = (By.CSS_SELECTOR, "div.popup_menu_icon.support_icon")
    __about_menu_item = (By.XPATH, "//a[text()='About your actiTIME']")
    __product_version_text = (By.CSS_SELECTOR, "span.productVersion")
    __close_button = (By.ID, "aboutPopupCloseButtonId")
    
    def click_on_help_menu(self):
        click(self.find_element(*self.__help_menu))
        
    def click_on_about_menu_item(self):
        click(self.find_element(*self.__about_menu_item))
        
    def get_product_version(self):
        value = text(self.find_element(*self.__product_version_text))
        return value
        
    def close_pop_up(self):
        click(self.find_element(*self.__close_button))
        