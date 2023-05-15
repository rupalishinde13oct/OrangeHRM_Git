import time

import pytest

from pageObjects.AddEmployee import AddEmployee
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchEmployee import SearchEmployee
from utilities.Logger import LegGenrator
from utilities.readproperties import ReadConfig


class Test_EmpSearch:

    url = ReadConfig.geturl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    log = LegGenrator.loggen()

    @pytest.mark.sanity
    def test_EmpSearch_005(self , setup):
        self.d = setup
        self.log.info("test_EmpSearch_005 is Started")
        self.log.info("Opening Browser..")
        self.d.get(self.url)
        self.log.info("Go To --> " +self.url)

        self.lp = LoginPage(self.d)
        time.sleep(2)
        self.lp.Enter_Username(self.username)
        self.log.info("Entering Username -->" +self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password -->" + self.password)
        self.lp.ClickLoginButton()
        self.log.info("Click on Login Button")
        time.sleep(2)
        self.ae = AddEmployee(self.d)
        self.ae.Click_On_PIM()
        self.log.info("Click on PIM Button")
        time.sleep(2)
        self.se = SearchEmployee(self.d)
        time.sleep(5)
        self.se.Enter_EmployeeName("David  Morris")
        self.log.info("Entering Employee name to search")
        time.sleep(2)
        self.se.Click_On_SearchButton()
        self.log.info("Click on search Button")
        time.sleep(5)

        self.se.Search_Emp_Status()
        if self.se.Search_Emp_Status() == True:
            self.log.info("Search Found")
            self.d.save_screenshot("E:\\OrangeHRM\\Screenshots\\test_EmpSearch_005_Pass.png")
            self.lp.ClickMenuButton()
            self.log.info("Click on Menu Button")
            self.lp.ClickLogoutButton()
            self.log.info("Click on Logout Button")
            self.log.info("test_EmpSearch_005 is Passed")
            assert True
        else:
            self.log.info("No Search Found")
            self.d.save_screenshot("E:\\OrangeHRM\\Screenshots\\test_EmpSearch_005_Fail.png")
            self.lp.ClickMenuButton()
            self.log.info("Click on Menu Button")
            self.lp.ClickLogoutButton()
            self.log.info("Click on Logout Button")
            self.log.info("test_EmpSearch_005 is Failed")
            assert False

        self.d.close()