from source.lib import constants
from source.pages.login_page import LoginPage
from source.lib import excel_automation as excel
from source.pages.home_page import HomePage


def test_TC001_valid_login_test(request):
    username = excel.get_cell_value(constants.EXCEL_PATH, "Login", 2, "UserName")
    password = excel.get_cell_value(constants.EXCEL_PATH, "Login", 2, "Password")
    expected_product_verion = excel.get_cell_value(constants.EXCEL_PATH, "Login", 2, "Expected_Result")
    
    l = LoginPage(request.node.driver)
    l.enter_username(username)
    l.enter_password(password)
    l.click_login_button()
    h = HomePage(request.node.driver)
    h.click_on_help_menu()
    h.click_on_about_menu_item()
    actual_product_version = h.get_product_version()
    
    assert actual_product_version == expected_product_verion, "Fail: Expected Product version is not displaying"
    h.close_pop_up()
    h.click_on_logout()
    