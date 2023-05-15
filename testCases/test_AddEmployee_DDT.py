import time

from pageObjects.AddEmployee import AddEmployee
from pageObjects.LoginPage import LoginPage
from utilities import XLutils
from utilities.Logger import LegGenrator

from utilities.readproperties import ReadConfig


class TestAddEmployee_DDT:

    url = ReadConfig.geturl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    log = LegGenrator.loggen()
    path = "E:\\OrangeHRM\\testCases\\TestData\\EmployeeList.xlsx"

    def test_AddEmployee_ddt_006(self ,setup):
        self.d = setup
        self.log.info("test_AddEmployee_ddt_006 is Started")
        self.log.info("Opening Browser")
        self.d.get(self.url)
        self.log.info("Go To --> " + self.url)

        self.lp = LoginPage(self.d)
        self.log.info("Login Page Opened")
        time.sleep(5)
        self.lp.Enter_Username(self.username)
        self.log.info("Username Entered -->" + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Password Entered -->" + self.password)
        self.lp.ClickLoginButton()
        self.log.info("Login Successful")

        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        print("No of Rows are -->" , self.rows)

        self.ae = AddEmployee(self.d)
        self.ae.Click_On_PIM()
        self.log.info("Clicked on PIM tab")
        time.sleep(5)
        self.ae.Click_Add_Employee()
        self.log.info("Clicked on Add Button")
        time.sleep(5)
        status_list = []
        for i in range(2,self.rows+1):
            self.First_Name = XLutils.readEmployeeList(self.path, 'Sheet1' , i , 2)
            self.Middle_Name = XLutils.readEmployeeList(self.path, 'Sheet1', i, 3)
            self.Last_Name = XLutils.readEmployeeList(self.path, 'Sheet1', i, 4)

            self.ae.Enter_First_Name(self.First_Name)
            self.log.info("First Name entered -->" + self.First_Name)
            self.ae.Enter_Middle_Name(self.Middle_Name)
            self.log.info("Middle Name entered -->" + self.Middle_Name)
            self.ae.Enter_Last_Name(self.Last_Name)
            self.log.info("Last Name entered -->" + self.Last_Name)
            time.sleep(2)
            self.ae.Click_Submit()
            self.log.info("Clicked On Submit Button")

            time.sleep(10)

            if self.ae.Add_Employee_Success() == True:
                self.d.save_screenshot("E:\\OrangeHRM\\Screenshots\\test_AddEmployee_ddt_006_Pass.png")
                self.ae.Click_ON_AddEmployee_Button()
                self.log.info("Clicked On Add_Employee Button")
                XLutils.writeDataToXL(self.path , 'Sheet1' , i , 5 , "Pass")
                self.log.info("Data is written in XL sheet")
                status_list.append("Pass")
                # time.sleep(2)

            else:
                self.d.save_screenshot("E:\\OrangeHRM\\Screenshots\\test_AddEmployee_ddt_006_Fail.png")
                XLutils.writeDataToXL(self.path , 'Sheet1' , i , 5 , "Fail")
                self.log.info("Data is written in XL sheet")
                status_list.append("Fail")


        print(status_list)
        time.sleep(2)
        self.lp.ClickMenuButton()
        self.log.info("Click on Menu Button")
        self.lp.ClickLogoutButton()
        self.log.info("Click on Logout Button")
        self.d.close()

        if "Fail" not in status_list:
            self.log.info("test_addEmp_ddt_005 is Passed")
            assert True
        else:
            self.log.info("test_addEmp_ddt_005 is Failed")
            assert False
        self.log.info("test_addEmp_ddt_005 is Completed")
