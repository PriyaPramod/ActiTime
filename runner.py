import pytest
from datetime import datetime
import os
from source.lib import constants


class MyPluggin:
    
    def pytest_sessionfinish(self):
        time_stamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        html_path = constants.ALLURE_REPORTS + time_stamp
        report_command = "allure generate " + constants.ALLURE_RESULTS + " --output " + html_path
        print(report_command)
        os.popen(report_command)


commands = ['-n','2','--alluredir', constants.ALLURE_RESULTS]

pytest.main(commands, plugins=[MyPluggin()])

'''
To re-run the framework -> --lf or --last-failed

'''
