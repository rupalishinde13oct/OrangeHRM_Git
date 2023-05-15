from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class AddEmployee:

    PIM_Button_PATH = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
    Add_Button_PATH = (By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']")

    First_Name_PATH = (By.XPATH, "//input[@placeholder='First Name']")
    Middle_Name_PATH = (By.XPATH, "//input[@placeholder='Middle Name']")
    Last_Name_PATH = (By.XPATH, "//input[@placeholder='Last Name']")
    Submit_Button_PATH = (By.XPATH, "//button[@type='submit']")
    SuccessMSG_PATH = (By.XPATH, "//h6[normalize-space()='Personal Details']")
    AddEmployee_Button_XPATH = (By.XPATH , "//a[normalize-space()='Add Employee']")

    def __init__(self , d):
        self.d = d

    def Click_On_PIM(self):
        self.d.find_element(*AddEmployee.PIM_Button_PATH).click()

    def Click_Add_Employee(self):
        self.d.find_element(*AddEmployee.Add_Button_PATH).click()

    def Enter_First_Name(self , firstname):
        self.d.find_element(*AddEmployee.First_Name_PATH).send_keys(firstname)

    def Enter_Middle_Name(self , middlename):
        self.d.find_element(*AddEmployee.Middle_Name_PATH).send_keys(middlename)

    def Enter_Last_Name(self , lastname):
        self.d.find_element(*AddEmployee.Last_Name_PATH).send_keys(lastname)

    def Click_Submit(self):
        self.d.find_element(*AddEmployee.Submit_Button_PATH).click()

    def Click_ON_AddEmployee_Button(self):
        self.d.find_element(*AddEmployee.AddEmployee_Button_XPATH).click()



    def Add_Employee_Success(self):
        self.d.implicitly_wait(10)
        try:

            self.d.find_element(*AddEmployee.SuccessMSG_PATH)
            return True
        except NoSuchElementException:
            return False