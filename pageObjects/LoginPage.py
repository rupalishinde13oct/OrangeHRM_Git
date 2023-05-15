import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:

    Username_XPATH = (By.XPATH , "//input[@placeholder='Username']")
    Password_XPATH = (By.XPATH, "//input[@placeholder='Password']")
    Login_Button_XPATH = (By.XPATH, "//button[@type='submit']")
    Menu_Button_XPATH = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    Logout_Button_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self , d):
        self.d = d

    def Enter_Username(self , username):
        self.d.find_element(*LoginPage.Username_XPATH).send_keys(username)

    def Enter_Password(self , password):
        self.d.find_element(*LoginPage.Password_XPATH).send_keys(password)

    def ClickLoginButton(self):
        self.d.find_element(*LoginPage.Login_Button_XPATH).click()
        time.sleep(3)

    def ClickMenuButton(self):
        self.d.find_element(*LoginPage.Menu_Button_XPATH).click()

    def ClickLogoutButton(self):
        self.d.find_element(*LoginPage.Logout_Button_XPATH).click()

    def Login_Status(self):
        self.d.implicitly_wait(10)
        try:
            self.d.find_element(*LoginPage.Menu_Button_XPATH)
            return True
        except NoSuchElementException:
            return False