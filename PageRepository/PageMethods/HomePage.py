import time
from selenium.webdriver.common.by import By
from PageRepository.PageMethods.BasePage import BasePage
from PageRepository.PageLocators.HomePageElements import HomePageElements


class HomePage(BasePage):

    elements = HomePageElements

    '''Constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)

    ''' Page Actions for Agent Home Page '''

    '''This is to check the title of the Page'''
    def get_home_page_title(self,title):
        return self.get_title(title)

    '''This is used to check the user internal chat icon'''
    def is_chat_icon_exist(self):
        return self.is_visible(self.elements.CHAT_ICON)

    ''' This is used to check HOME TAB Link'''
    def is_home_tab_exist(self):
        return self.is_visible(self.elements.HOME_TAB)

    def is_call_details_tab_exist(self):
        return self.is_visible(self.elements.CALL_DETAILS_TAB)

    def get_agent_name_value(self):
        if self.is_visible(self.elements.AGENT_NAME):
            return self.get_element_text(self.elements.AGENT_NAME)

    def get_agent_status(self):
        if self.is_visible(self.elements.AGENT_STATUS):
            return self.get_element_text(self.elements.AGENT_STATUS)

    def is_call_button_disabled(self):
        self.do_click(self.elements.TELEPHONE_PANEL_BUTTON)
        flag = self.is_attribute_present_in_element(self.elements.CALL_BUTTON, 'disabled')
        self.do_click(self.elements.TELEPHONE_PANEL_BUTTON)
        return flag

    def do_agent_available(self):
        self.do_click(self.elements.AGENT_STATUS_DROPDOWN)
        self.do_click(self.elements.AVAILABLE_STATUS)

    def is_agent_auto_call_on(self):
        self.do_click(self.elements.AGENT_AUTO_CALL_DROPDOWN)
        return self.is_attribute_present_in_element(self.elements.AGENT_AUTO_CALL_STATUS, "checked")

    def do_manual_dial_phone(self, customer_phone):
        self.do_click(self.elements.TELEPHONE_PANEL_BUTTON)
        self.do_click(self.elements.PHONE_INPUT)
        self.do_send_keys(self.elements.PHONE_INPUT, customer_phone)
        self.do_click(self.elements.CALL_BUTTON)
        self.do_click(self.elements.DIAL_ONLY_BUTTON)
        time.sleep(10)

    def wait_for_call_status(self, expected_text, timeout=30):
        self.wait_for_element_text(self.elements.CALL_STATUS, expected_text, timeout)

    def get_call_status(self):
        return self.get_element_text(self.elements.CALL_STATUS)

    def do_dispose_call(self, disposition_class, disposition_code):
        self.do_click(self.elements.DISPOSE_PAGE_BUTTON)
        self.do_click(self.elements.DISPOSITION_CLASS_DROPDOWN)
        self.select_item_from_dropdown_list(self.elements.DISPOSITION_CLASS_LIST, disposition_class)
        self.do_click(self.elements.SUB_DISPOSITION_DROPDOWN)
        self.select_item_from_dropdown_list(self.elements.DISPOSITION_CODE_LIST, disposition_code)
        self.do_click(self.elements.SAVE_DISPOSE_BUTTON)

    def do_end_call(self):
        self.do_click(self.elements.END_CALL_BUTTON)