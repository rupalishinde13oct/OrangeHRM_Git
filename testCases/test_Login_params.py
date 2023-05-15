import time

from pageObjects.LoginPage import LoginPage
from utilities.Logger import LegGenrator
from utilities.readproperties import ReadConfig


class Test_Login_Params:

    url = ReadConfig.geturl()
    # username = ReadConfig.getusername()
    # password = ReadConfig.getpassword()
    log = LegGenrator.loggen()

    def test_Login_Params_004(self , setup , getLoginData):

        self.d = setup
        self.log.info("test_Login_002 is Started")
        self.log.info("Opening Browser")
        self.d.get(self.url)
        self.log.info("Go to -->" +self.url)
        self.lp = LoginPage(self.d)
        self.log.info("Login Page Opened")
        time.sleep(5)
        self.lp.Enter_Username(getLoginData[0])
        self.log.info("Username Entered -->"+getLoginData[0])
        self.lp.Enter_Password(getLoginData[1])
        self.log.info("Password Entered -->" + getLoginData[1])
        self.lp.ClickLoginButton()


        if self.lp.Login_Status() == True:
            if getLoginData[2] == "Pass":
                self.log.info("Login Successful")
                self.log.info("test_Login_002 is Passed")
                self.d.save_screenshot("E:\\OrangeHRM\\Screenshots\\"+getLoginData[0]+getLoginData[1]+"test_Login_Params_004_pass.png")
                self.lp.ClickMenuButton()
                self.log.info("Clicked on Logout")
                self.lp.ClickLogoutButton()
                assert True
            else:
                self.log.info("test_Login_002 is Failed")
                self.d.save_screenshot(
                    "E:\\OrangeHRM\\Screenshots\\"+getLoginData[0]+getLoginData[1]+"test_Login_Params_004_fail.png")
                assert False
        else:
            if getLoginData[2] == "Fail":
                self.log.info("test_Login_002 is Passed")
                assert True

            else:
                self.log.info("test_Login_002 is Failed")
                self.d.save_screenshot("E:\\OrangeHRM\\Screenshots\\"+getLoginData[0]+getLoginData[1]+"test_Login_Params_004_fail.png")
                assert False

        self.d.close()
        self.log.info("test_Login_002 is Completed")



