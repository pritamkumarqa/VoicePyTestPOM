from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.WorkingModePage import WorkingModePage

class LoginPage(BasePage):

    '''By Locaotrs OR XPath'''
    USERNAME = (By.XPATH, "//input[@automationid='enterLoginUsername']")
    PASSWORD = (By.XPATH, "//input[@automationid='enterLoginPassword']")
    LOGIN_BUTTON = (By.XPATH, "//button[@automationid='loginButton']")
    GOOGLE_SSO_BUTTON = (By.XPATH, "//button[@automationid='googlePlusLoginLoginBtn']")
    SAML_SSO_BUTTON = (By.XPATH, "//button[@automationid='SAMLLoginBtn']")
    FORCE_LOGIN_PAGE_HEADING = (By.XPATH, "//h2[@automationid='confirmationModalTitle' and text()='Force Login']")
    WORKMODE_PAGE_HEADING = (By.XPATH, "//h2[text()='Working Mode Selection']")
    FORCE_LOGIN_OK_BUTTON = (By.XPATH, "//button[@automationid='confirmationBtn1']")
    CAMPAIGN_SELECT_PAGE = (By.XPATH, "//h2[@automationid='campaignSelectionHeader']")
    VOICE_CAMPAIGN_INPUT = (By.XPATH, "//input[@type='search' and @placeholder='Select Voice Campaign']")
    VOICE_CAMPAIGN_LIST = (By.XPATH, "//li[@role='treeitem']")
    CAMPAIGN_SELECT_NEXT_BUTTON = (By.XPATH, "//button[@automationid='camapignSaveBtn' and span[text()='Next']]")
    WORK_MODE = (By.XPATH, "//input[@type='radio' and @name='workingMode']/following-sibling::label")
    #WORK_MODE = (By.XPATH, "//span[input[@type='radio' and @name='workingMode']]/label")
    WORK_MODE_SELECT_NEXT_BUTTON = (By.XPATH, "//button[span[text()='Next']]")
    EXTENSION_SEARCH = (By.XPATH, "//div[@automationid='extensionSelectionList']//span[@title='Select Extension']")
    EXTENSION_LIST = (By.XPATH, "//span[input[@type='search']]/following-sibling::span/ul[@role='tree']/li[@role='treeitem']")
    EXTENSION_PHONE_INPUT = (By.XPATH, "//input[@placeholder='Enter Number']")
    EXTENSION_SELECT_DONE_BUTTON = (By.XPATH, "//button[@automationid='extensionSaveBtn']")


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
        return self.is_visible(self.GOOGLE_SSO_BUTTON)

    ''' This is used to check SAML SSO Login Link'''
    def is_saml_sso_button_exist(self):
        return self.is_visible(self.SAML_SSO_BUTTON)

    '''This is used to login to application'''
    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        if self.is_force_login_page_displayed():
            return "forcelogin"
        elif self.is_workmode_page_displayed():
            return "workmode"
        else:
            return "unknown"

    def do_force_login(self):
        if self.is_force_login_page_displayed():
            self.do_click(self.FORCE_LOGIN_OK_BUTTON)
            if self.is_workmode_page_displayed():
                return "workmode"
            else:
                return "workmode_page_error"
        else:
            return "unknown"


    def is_force_login_page_displayed(self):
        # Check for elements on the force login page
        return self.is_visible(self.FORCE_LOGIN_PAGE_HEADING)

    def is_workmode_page_displayed(self):
        # Check for elements on the working mode page
        return self.is_visible(self.WORKMODE_PAGE_HEADING)

    def do_work_mode_select(self, user_working_mode):
        self.select_item_from_dropdown_list(self.WORK_MODE,user_working_mode)
        self.do_click(self.WORK_MODE_SELECT_NEXT_BUTTON)
        if self.is_campaign_select_page_displayed():
            return True
        else:
            return False

    def is_campaign_select_page_displayed(self):
        # Check for elements on the working mode page
        return self.is_visible(self.CAMPAIGN_SELECT_PAGE)

    def do_voice_campaign_select(self, campaign_name):
        self.do_click(self.VOICE_CAMPAIGN_INPUT)
        self.select_item_from_dropdown_list(self.VOICE_CAMPAIGN_LIST,campaign_name)
        self.do_click(self.CAMPAIGN_SELECT_NEXT_BUTTON)

    def do_extension_select(self, user_extension,user_phone):
        self.do_click(self.EXTENSION_SEARCH)
        self.select_item_from_dropdown_list(self.EXTENSION_LIST,user_extension)
        self.do_send_keys(self.EXTENSION_PHONE_INPUT, user_phone)
        self.do_click(self.EXTENSION_SELECT_DONE_BUTTON)

        
