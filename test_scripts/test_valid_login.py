from source.lib import constants
from source.pages.login_page import LoginPage
from source.lib import excel_automation as excel


def test_TC001_valid_login_test(request):
    username = excel.get_cell_value(constants.EXCEL_PATH, "Login", 
                                    0, "UserName")
    password = excel.get_cell_value(constants.EXCEL_PATH, "Login", 
                                    0, "Password")
    excpected_title = excel.get_cell_value(constants.EXCEL_PATH, "Login", 
                                           0, "Expected_Result")
    
    l = LoginPage(request.node.driver)
    l.enter_username(username)
    l.enter_password(password)
    l.click_login_button()
    flag = l.verify_title(excpected_title)
    assert flag , "Fail: Title is not matching, Home page is not displayed"
    l.click_on_logout()