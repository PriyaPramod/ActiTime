from source.lib import constants
from source.pages.login_page import LoginPage
from source.lib import excel_automation as excel


def test_TC001_valid_login_test(request):
    username = excel.get_cell_value(constants.EXCEL_PATH, "Login", 1, "UserName")
    password = excel.get_cell_value(constants.EXCEL_PATH, "Login", 1, "Password")
    expected_error_message = excel.get_cell_value(constants.EXCEL_PATH, "Login", 1, "Expected_Result")
    
    l = LoginPage(request.node.driver)
    l.enter_username(username)
    l.enter_password(password)
    l.click_login_button()
    actual_error_message = l.get_error_message()
    
    assert actual_error_message == expected_error_message, "Fail: Error message is not displaying"