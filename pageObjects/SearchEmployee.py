from selenium.webdriver.common.by import By


class SearchEmployee:

    EmployeeName_XPATH = (By.XPATH , "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
    Search_Button_XPATH = (By.XPATH , "//button[@type='submit']")
    Search_Status_CSS = (By.CSS_SELECTOR , "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)")


    def __init__(self , d):
        self.d = d

    def Enter_EmployeeName(self , empname):
        self.d.find_element(*SearchEmployee.EmployeeName_XPATH).send_keys(empname)

    def Click_On_SearchButton(self):
        self.d.find_element(*SearchEmployee.Search_Button_XPATH).click()

    def Search_Emp_Status(self):
        search = self.d.find_elements(*SearchEmployee.Search_Status_CSS)
        l = len(search)
        if l == 0:
            return False
        elif l >= 1:
            # print(self.d.find_element(*SearchEmployee.Search_Status_CSS).text)
            return True





