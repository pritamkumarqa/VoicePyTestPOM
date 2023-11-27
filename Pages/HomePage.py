import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class HomePage(BasePage):

    '''By Locaotrs OR XPath'''
    HOME_TAB = (By.XPATH, "//a[@automationid='agentHomeTab' and span[text()='Home']]")
    KNOWLEDGE_BASE = (By.XPATH, "//a[@span[text()='Knowledge Base']]")
    CALL_DETAILS_TAB = (By.XPATH, "//a[@automationid='agentCallDetailsTab' and span[text()='Call Details']]")
    CHAT_ICON = (By.XPATH, "//a[@class='btn-internal-chat']")
    AGENT_NAME=(By.XPATH, "//a[@automationid='userNameLink']/span")
    AGENT_STATUS = (By.XPATH, "//a[@automationid='agentAvailibilityStatusDropdown']/span")
    AGENT_STATUS_DROPDOWN = (By.XPATH, "//a[@automationid='agentAvailibilityStatusDropdown']")
    AVAILABLE_STATUS = (By.XPATH, "//li[a[@automationid='Available']]")
    AGENT_AUTO_CALL_DROPDOWN = (By.XPATH, "//div[contains(@class,'switch-mode')]//a[contains(@class,'dropdown-button')]")
    AGENT_AUTO_CALL_TOGGLE = (By.XPATH, "//div[@id='automode']//span[@class='lever']")
    AGENT_AUTO_CALL_STATUS = (By.XPATH, "//div[@id='automode']//label[span[text()='Voice']]/input[@type = 'checkbox']")
    '''Telephony panel related locators'''
    TELEPHONE_PANEL_BUTTON = (By.XPATH, "//a[@automationid='callPanelIcon']")
    PHONE_INPUT = (By.XPATH,
                   "//div[@automationid='callPanelBox']//div[@automationid='search']//input[@placeholder='Search for customer']")
    CALL_BUTTON = (By.XPATH, "//div[@automationid='callPanelBox']//button[@automationid='callBtn']")
    DIAL_ONLY_BUTTON = (By.XPATH, "//button[@automationid='confirmationBtn2' and span[text()='Dial only']]")
    CREATE_DIAL_BUTTON = (By.XPATH, "//button[@automationid='confirmationBtn1']//span[text()='Create and Dial']")
    CANCEL_BUTTON = (
        By.XPATH, "//button[@automationid='confirmationBtn2']/following-sibling::button/span[text()='Cancel']")
    END_CALL_BUTTON = (
        By.XPATH, "//div[@automationid='callPanelBox']//button[@automationid='endCallBtn' and @title='End Call']")
    DISPOSE_PAGE_BUTTON = (
        By.XPATH,
        "//div[@automationid='callPanelBox']//button[i[@class='fontello fontellodisposition material-icons']]")
    # SELECT_DISPOSITION_CLASS_DROPDOWN = (
    # By.XPATH, "//span[@automationid='dispositionClassesShowListItems' and text()='Select a Disposition']")
    DISPOSITION_CLASS_DROPDOWN = (
        By.XPATH, "//*[@automationid='dispositionClassesShowListItems' and text()='Select a Disposition']")
    DISPOSITION_CLASS_LIST = (By.XPATH, "//ul[@role='tree']/li[@role='treeitem']")
    # DISPOSITION_CLASS = (
    #     By.XPATH, f"//ul[@role='tree']/li[@role='treeitem' and text()='{TestData.selected_disposition_class}']")
    SUB_DISPOSITION_DROPDOWN = (
        By.XPATH, "//span[@automationid='dispositionCodesShowListItems' and text()='Select a Sub Disposition']")
    DISPOSITION_CODE_LIST = (By.XPATH,
                             "//ul[li[text()='Select a Sub Disposition']]//li[@role='group']//li[@role='treeitem']")
    # DISPOSITION_CODE = (By.XPATH,
    #                     f"//ul[@role='tree' and li[text()='Select a Sub Disposition']]//li[@role='group' and strong[text()='{TestData.selected_disposition_class}']]//li[@role='treeitem' and text()='{TestData.selected_disposition_code}']")
    SAVE_DISPOSE_BUTTON = (By.XPATH, "//div[@automationid='callPanelBox']//button[@automationid='saveAndDisposeBtn']")
    CALL_STATUS = (By.XPATH, "//span[@automationid='callStatus']")

    '''Constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)

    ''' Page Actions for Agent Home Page '''

    def get_home_page_title(self,title):
        return self.get_title(title)

    '''This is used to check the user internal chat icon'''
    def is_chat_icon_exist(self):
        return self.is_visible(self.CHAT_ICON)

    ''' This is used to check HOME TAB Link'''
    def is_home_tab_exist(self):
        return self.is_visible(self.HOME_TAB)

    def is_call_details_tab_exist(self):
        return self.is_visible(self.CALL_DETAILS_TAB)

    def get_agent_name_value(self):
        if self.is_visible(self.AGENT_NAME):
            return self.get_element_text(self.AGENT_NAME)

    def get_agent_status(self):
        if self.is_visible(self.AGENT_STATUS):
            return self.get_element_text(self.AGENT_STATUS)

    def is_call_button_disabled(self):
        self.do_click(self.TELEPHONE_PANEL_BUTTON)
        flag = self.is_attribute_present_in_element(self.CALL_BUTTON, 'disabled')
        self.do_click(self.TELEPHONE_PANEL_BUTTON)
        return flag

    def do_agent_available(self):
        self.do_click(self.AGENT_STATUS_DROPDOWN)
        self.do_click(self.AVAILABLE_STATUS)

    def is_agent_auto_call_on(self):
        self.do_click(self.AGENT_AUTO_CALL_DROPDOWN)
        return self.is_attribute_present_in_element(self.AGENT_AUTO_CALL_STATUS, "checked")

    def do_manual_dial_phone(self, customer_phone):
        self.do_click(self.TELEPHONE_PANEL_BUTTON)
        self.do_click(self.PHONE_INPUT)
        self.do_send_keys(self.PHONE_INPUT, customer_phone)
        self.do_click(self.CALL_BUTTON)
        self.do_click(self.DIAL_ONLY_BUTTON)
        time.sleep(10)

    def wait_for_call_status(self, expected_text, timeout=30):
        self.wait_for_element_text(self.CALL_STATUS, expected_text, timeout)

    def get_call_status(self):
        return self.get_element_text(self.CALL_STATUS)

    def do_dispose_call(self, disposition_class, disposition_code):
        self.do_click(self.DISPOSE_PAGE_BUTTON)
        self.do_click(self.DISPOSITION_CLASS_DROPDOWN)
        self.select_item_from_dropdown_list(self.DISPOSITION_CLASS_LIST, disposition_class)
        self.do_click(self.SUB_DISPOSITION_DROPDOWN)
        self.select_item_from_dropdown_list(self.DISPOSITION_CODE_LIST, disposition_code)
        self.do_click(self.SAVE_DISPOSE_BUTTON)

    def do_end_call(self):
        self.do_click(self.END_CALL_BUTTON)