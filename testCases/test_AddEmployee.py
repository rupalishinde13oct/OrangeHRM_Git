import time

import pytest

from pageObjects.AddEmployee import AddEmployee
from pageObjects.LoginPage import LoginPage
from utilities.Logger import LegGenrator
from utilities.readproperties import ReadConfig


class Test_AddEmployee:

    url = ReadConfig.geturl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    log = LegGenrator.loggen()

    @pytest.mark.sanity
    def test_AddEmployee_003(self , setup):
        self.d = setup
        self.log.info("test_AddEmployee is Started")
        self.log.info("Opening Browser")
        self.d.get(self.url)
        self.log.info("Go To --> "+self.url)

        self.lp = LoginPage(self.d)
        self.log.info("Login Page Opened")
        time.sleep(5)
        self.lp.Enter_Username(self.username)
        self.log.info("Username Entered -->" + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Password Entered -->" + self.password)
        self.lp.ClickLoginButton()
        self.log.info("Login Successful")
        # time.sleep(2)
        self.ae = AddEmployee(self.d)
        self.ae.Click_On_PIM()
        self.log.info("Clicked on PIM tab")
        time.sleep(5)
        self.ae.Click_Add_Employee()
        self.log.info("Clicked on Add Button")
        time.sleep(5)
        self.ae.Enter_First_Name("Rupali")
        self.log.info("First Name entered")
        self.ae.Enter_Middle_Name("P")
        self.log.info("Middle Name entered")
        self.ae.Enter_Last_Name("Pandit")
        self.log.info("Last Name entered")
        self.ae.Click_Submit()
        self.log.info("Clicked On Submit Button")

        if self.ae.Add_Employee_Success() == True:
            self.log.info("test_AddEmployee is Passed")
            self.lp.ClickMenuButton()
            self.log.info("Click on Logout Button")
            self.lp.ClickLogoutButton()
            assert True
        else:
            self.log.info("test_AddEmployee is Failed")
            assert False
        self.d.close()
        self.log.info("test_AddEmployee is Completed")

