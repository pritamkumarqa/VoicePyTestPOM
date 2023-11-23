import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Config.config import TestData

@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):
    print("Initializing driver...")
    if request.param == "chrome":
        s = Service(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        web_driver = webdriver.Chrome(service=s)
        # web_driver = webdriver.Chrome()
        # web_driver.maximize_window()
    # if request.param == "firefox":
    #     web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    web_driver.maximize_window()
    web_driver.get(TestData.BASE_URL)
    request.cls.driver = web_driver
    yield
    web_driver.close()
    print("Closing driver...")