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

