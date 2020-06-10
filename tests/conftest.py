import pytest
from selenium import webdriver


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp - conftest.py file")

    if browser == 'chrome':
        baseURL = "https://letskodeit.teachable.com"
        chromeDriverPath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chromeDriverPath)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        print("Running tests on Chrome")
    elif browser == 'firefox':
        baseURL = "https://letskodeit.teachable.com"
        firefoxDriverPath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\geckodriver.exe"
        driver = webdriver.Firefox(executable_path=firefoxDriverPath)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        print("Running tests on Firefox")
    else:
        #driver = webdriver.Ie
        print("Invalid browser name given")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")