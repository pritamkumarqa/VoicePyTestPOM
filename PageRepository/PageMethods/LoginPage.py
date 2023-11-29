from selenium.webdriver.common.by import By

from PageRepository.PageMethods.BasePage import BasePage
from PageRepository.PageMethods.HomePage import HomePage
from PageRepository.PageLocators.LoginPageElements import LoginPageElements


class LoginPage(BasePage):

    elements = LoginPageElements

    '''Constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)

    ''' Page Actions for Login Page '''

    '''This is used to get the login page title'''
    def get_login_page_title(self, title):
        return self.get_title(title)

    ''' This is used to check Google SSO Login Link'''
    def is_google_sso_button_exist(self):
        return self.is_visible(self.elements.GOOGLE_SSO_BUTTON)

    ''' This is used to check SAML SSO Login Link'''
    def is_saml_sso_button_exist(self):
        return self.is_visible(self.elements.SAML_SSO_BUTTON)

    '''This is used to login to application'''
    def do_login(self, username, password):
        self.do_send_keys(self.elements.USERNAME, username)
        self.do_send_keys(self.elements.PASSWORD, password)
        self.do_click(self.elements.LOGIN_BUTTON)
        if self.is_force_login_page_displayed():
            return "forcelogin"
        elif self.is_workmode_page_displayed():
            return "workmode"
        else:
            return "unknown"

    def do_force_login(self):
        if self.is_force_login_page_displayed():
            self.do_click(self.elements.FORCE_LOGIN_OK_BUTTON)
            if self.is_workmode_page_displayed():
                return "workmode"
            else:
                return "workmode_page_error"
        else:
            return "unknown"


    def is_force_login_page_displayed(self):
        # Check for elements on the force login page
        return self.is_visible(self.elements.FORCE_LOGIN_PAGE_HEADING)

    def is_workmode_page_displayed(self):
        # Check for elements on the working mode page
        return self.is_visible(self.elements.WORKMODE_PAGE_HEADING)

    def do_work_mode_select(self, user_working_mode):
        self.select_item_from_dropdown_list(self.elements.WORK_MODE,user_working_mode)
        self.do_click(self.elements.WORK_MODE_SELECT_NEXT_BUTTON)
        if self.is_campaign_select_page_displayed():
            return True
        else:
            return False

    def is_campaign_select_page_displayed(self):
        # Check for elements on the working mode page
        return self.is_visible(self.elements.CAMPAIGN_SELECT_PAGE)

    def do_voice_campaign_select(self, campaign_name):
        self.do_click(self.elements.VOICE_CAMPAIGN_INPUT)
        self.select_item_from_dropdown_list(self.elements.VOICE_CAMPAIGN_LIST,campaign_name)
        self.do_click(self.elements.CAMPAIGN_SELECT_NEXT_BUTTON)
        if self.is_extension_select_page_displayed():
            return True
        elif HomePage(self.driver).is_call_details_tab_exist():
            return True
        else:
            return False

    def is_extension_select_page_displayed(self):
        # Check for elements on the working mode page
        return self.is_visible(self.elements.EXTENSION_SELECT_PAGE)

    def do_extension_select(self, user_extension,user_phone):
        if self.is_extension_select_page_displayed():
            self.do_click(self.elements.EXTENSION_SEARCH)
            self.select_item_from_dropdown_list(self.elements.EXTENSION_LIST, user_extension)
            self.do_send_keys(self.elements.EXTENSION_PHONE_INPUT, user_phone)
            self.do_click(self.elements.EXTENSION_SELECT_DONE_BUTTON)
            if HomePage(self.driver).is_call_details_tab_exist():
                return True
            else:
                return False
        else:
            return False

    def do_logout(self):
        self.do_click(self.elements.AGENT_PREFRENCE_DROPDOWN)
        self.do_click(self.elements.LOGOUT_BUTTON)


    def do_agent_complete_login(self, username, password,user_working_mode,campaign_name,user_extension,user_phone):
        self.do_send_keys(self.elements.USERNAME, username)
        self.do_send_keys(self.elements.PASSWORD, password)
        self.do_click(self.elements.LOGIN_BUTTON)
        if self.is_force_login_page_displayed():
            self.do_click(self.elements.FORCE_LOGIN_OK_BUTTON)
        if self.is_workmode_page_displayed():
            self.select_item_from_dropdown_list(self.elements.WORK_MODE, user_working_mode)
            self.do_click(self.elements.WORK_MODE_SELECT_NEXT_BUTTON)
        if self.is_campaign_select_page_displayed():
            self.do_click(self.elements.VOICE_CAMPAIGN_INPUT)
            self.select_item_from_dropdown_list(self.elements.VOICE_CAMPAIGN_LIST, campaign_name)
            self.do_click(self.elements.CAMPAIGN_SELECT_NEXT_BUTTON)
        if self.is_extension_select_page_displayed():
            self.do_click(self.elements.EXTENSION_SEARCH)
            self.select_item_from_dropdown_list(self.elements.EXTENSION_LIST, user_extension)
            self.do_send_keys(self.elements.EXTENSION_PHONE_INPUT, user_phone)
            self.do_click(self.elements.EXTENSION_SELECT_DONE_BUTTON)
        return HomePage(self.driver)
