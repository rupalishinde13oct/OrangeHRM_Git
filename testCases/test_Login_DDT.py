import time

from pageObjects.LoginPage import LoginPage
from utilities import XLutils
from utilities.Logger import LegGenrator
from utilities.readproperties import ReadConfig


class Test_Login_DDT:

    url = ReadConfig.geturl()
    # username = ReadConfig.getusername()
    # password = ReadConfig.getpassword()
    log = LegGenrator.loggen()
    path = "E:\\OrangeHRM\\testCases\\TestData\\LoginData.xlsx"


    def test_Login_ddt_007(self , setup):

        self.d = setup
        self.log.info("test_Login_002 is Started")
        self.log.info("Opening Browser")
        self.d.get(self.url)
        self.log.info("Go to -->" +self.url)
        self.lp = LoginPage(self.d)
        self.log.info("Login Page Opened")
        time.sleep(5)

        self.row = XLutils.getrowCount(self.path , 'Sheet1')
        print(self.row)

        for i in range(2,self.row+1):
            self.username = XLutils.readEmployeeList(self.path , 'Sheet1' , i , 2)
            self.password = XLutils.readEmployeeList(self.path, 'Sheet1', i, 3)
            self.d.implicitly_wait(10)
            self.lp.Enter_Username(self.username)
            self.log.info("Username Entered -->"+self.username)
            self.lp.Enter_Password(self.password)
            self.log.info("Password Entered -->" + self.password)
            self.lp.ClickLoginButton()


            if self.lp.Login_Status() == True:
                XLutils.writeDataToXL(self.path , 'Sheet1' , i , 4 , 'Pass')
                self.log.info("Login Successful")
                self.log.info("test_Login_002 is Passed")
                self.d.save_screenshot("E:\\OrangeHRM\\Screenshots\\"+self.username+self.password+"test_Login_ddt_007_pass.png")
                self.lp.ClickMenuButton()
                self.log.info("Clicked on Logout")
                self.lp.ClickLogoutButton()

            else:
                XLutils.writeDataToXL(self.path, 'Sheet1', i, 4, 'Fail')
                self.log.info("test_Login_002 is Failed")
                self.d.save_screenshot(
                    "E:\\OrangeHRM\\Screenshots\\"+self.username+self.password+"test_Login_ddt_007_fail.png")


        self.d.close()
        self.log.info("test_Login_002 is Completed")



