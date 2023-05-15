import pytest
from attr.converters import optional
from selenium import webdriver
from selenium.webdriver import chrome, firefox, edge

#for multiple parameters use in code
@pytest.fixture(params=[
    ("Admin" , "admin123" , "Pass"),
    ("Admin1" , "admin123" , "Fail"),
    ("Admin" , "admin1231" , "Fail"),
    ("Admin1" , "admin1231" , "Fail"),
])

def getLoginData(request):
    return request.param


#For Cross-browers

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("Chrome Browser....")
        d = webdriver.Chrome()

    elif browser == 'firefox':
        print("Firefox Browser...")
        d = webdriver.Firefox()

    elif browser == 'edge':
        print("Edge Browser...")
        d = webdriver.Edge()

    else:
        print("Headless Mode...")
        opt = webdriver.ChromeOptions()
        opt.add_argument("headless")
        d = webdriver.Chrome(options=opt)

        d.implicitly_wait(10)
    return d


#To edit variables on reports

def pytest_metadata(metadata):
    metadata["Envirnment"] = "Test"
    metadata["Tester"] = "Rupali Pandit"
    metadata["Project"] = "OrangeHRM"

    metadata.pop("Packages" , None)