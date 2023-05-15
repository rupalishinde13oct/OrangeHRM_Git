import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.Logger import LegGenrator
from utilities.readproperties import ReadConfig


class Test_Login:

    url = ReadConfig.geturl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    log = LegGenrator.loggen()

    def test_page_Titl_001(self , setup):
        self.d = setup
        self.log.info("test_page_Titl_001 is Started")
        self.log.info("Opening Browser")
        self.d.get(self.url)
        self.log.info("Go to -->"+ self.url)
        if self.d.title == "OrangeHRM":
            assert True
            self.log.info("test_page_Titl_001 is Passed")
            self.log.info("Page Title is --> " + self.d.title)
        else:
            assert False
            self.log.info("test_page_Titl_001 is Failed")

        self.d.close()
        self.log.info("test_page_Titl_001 is Completed")

    @pytest.mark.sanity
    def test_Login_002(self , setup):

        self.d = setup
        self.log.info("test_Login_002 is Started")
        self.log.info("Opening Browser")
        self.d.get(self.url)
        self.log.info("Go to -->" +self.url)
        self.lp = LoginPage(self.d)
        self.log.info("Login Page Opened")
        time.sleep(5)
        self.lp.Enter_Username(self.username)
        self.log.info("Username Entered -->"+self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Password Entered -->" + self.password)
        self.lp.ClickLoginButton()


        if self.lp.Login_Status() == True:
            self.log.info("Login Successful")
            self.log.info("test_Login_002 is Passed")
            self.d.save_screenshot("E:\\OrangeHRM\\Screenshots\\test_Login_002_pass.png")
            self.lp.ClickMenuButton()
            self.log.info("Clicked on Logout")
            self.lp.ClickLogoutButton()
            assert True
        else:
            self.log.info("test_Login_002 is Failed")
            self.d.save_screenshot(
                "E:\\OrangeHRM\\Screenshots\\test_Login_002_fail.png")
            assert False

        self.d.close()
        self.log.info("test_Login_002 is Completed")



