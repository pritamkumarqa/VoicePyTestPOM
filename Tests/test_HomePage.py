import time

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class Test_Home(BaseTest):

    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_agent_complete_login(TestData.USER_NAME, TestData.PASSWORD, TestData.SELECTED_WORKING_MODE,
                                               TestData.CAMPAIGN_NAME, TestData.AGENT_RON_EXTENSION,
                                               TestData.AGENT_RON_PHONE)
        title = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_agent_name_in_preference(self):
        homePage = HomePage(self.driver)
        agent_name = homePage.get_agent_name_value()
        assert agent_name == TestData.USER_NAME

    def test_chat_icon(self):
        homePage = HomePage(self.driver)
        assert homePage.is_chat_icon_exist()

    def test_home_tab(self):
        homePage = HomePage(self.driver)
        assert homePage.is_home_tab_exist()

    def test_call_details_tab(self):
        homePage = HomePage(self.driver)
        assert homePage.is_call_details_tab_exist()

    def test_agent_status_just_after_login(self):
        homePage = HomePage(self.driver)
        agent_status = homePage.get_agent_status()
        print(f"agent status before status change is {agent_status} ")
        assert agent_status == "Just Logged In"

    def test_call_button_disabled(self):
        homePage = HomePage(self.driver)
        assert homePage.is_call_button_disabled()

    def test_agent_status_change_to_available(self):
        homePage = HomePage(self.driver)
        homePage.do_agent_available()
        agent_status = homePage.get_agent_status()
        print(f"agent status after status change is {agent_status} ")
        assert agent_status == "Available"

    def test_agent_auto_call_status_on(self):
        homePage = HomePage(self.driver)
        assert homePage.is_agent_auto_call_on()

    def test_manual_dial_phone(self):
        homePage = HomePage(self.driver)
        homePage.do_manual_dial_phone(TestData.CUSTOMER_PHONE)
        # Wait for the call status to change to 'Connected'
        homePage.wait_for_call_status('Connected')
        # Now, you can assert that the call status is 'Connected'
        call_status = homePage.get_call_status()
        assert call_status == 'Connected'


    def test_dispose_call(self):
        homePage = HomePage(self.driver)
        homePage.do_dispose_call(TestData.DISPOSITION_CLASS, TestData.DISPOSITION_CODE)
        time.sleep(10)

    def test_end_call(self):
        homePage = HomePage(self.driver)
        homePage.do_end_call()

    def test_logout(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_logout()
        time.sleep(10)