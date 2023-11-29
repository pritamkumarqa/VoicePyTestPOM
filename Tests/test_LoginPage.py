import time

from Config.config import TestData
from PageRepository.PageMethods.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):
    def test_google_sso_button_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_google_sso_button_exist()
        assert flag

    def test_saml_sso_button_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_saml_sso_button_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    # def test_login_valid_user_invalid_passwd(self):


    def test_login_success(self):
        self.loginPage = LoginPage(self.driver)
        login_result = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert login_result in ('forcelogin', 'workmode'), "Login result is unrecognized"
        if login_result == "forcelogin":
            print("ForceLogin pop-up is present after Login Operation")

        elif login_result == "workmode":
            print("WorkMode screen is present direct after Login Operation i.e without Force Login")

    def test_force_login(self):
        self.loginPage = LoginPage(self.driver)
        force_login_result = self.loginPage.do_force_login()
        if force_login_result == "workmode":
            print("Working Mode is present after Force Login Operation")
        elif force_login_result == "workmode_page_error":
            print("After force login working mode screen not visible")
        else:
            print("Force Login window not appeared so test case is failed which is fine")
        assert force_login_result in (
            'workmode'), "Either Force Login window not appeared OR after force login work mode not visible"

    def test_work_mode_select(self):
        self.loginPage = LoginPage(self.driver)
        work_mode_select_result = self.loginPage.do_work_mode_select(TestData.SELECTED_WORKING_MODE)
        assert work_mode_select_result, "Campaign Select Page is not displayed after work mode selection"

    def test_voice_campaign_select(self):
        self.loginPage = LoginPage(self.driver)
        campaign_select_result = self.loginPage.do_voice_campaign_select(TestData.CAMPAIGN_NAME)
        assert campaign_select_result

    def test_extension_select(self):
        self.loginPage = LoginPage(self.driver)
        extension_select_result = self.loginPage.do_extension_select(TestData.AGENT_RON_EXTENSION,
                                                                     TestData.AGENT_RON_PHONE)
        assert extension_select_result,"Extension select popup not came so webrtc"
        time.sleep(5)

    def test_logout(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_logout()
        time.sleep(10)
