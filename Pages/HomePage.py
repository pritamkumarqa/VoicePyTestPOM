from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class HomePage(BasePage):

    '''By Locaotrs OR XPath'''
    HOME_TAB = (By.XPATH, "//a[@automationid='agentHomeTab' and span[text()='Home']]")
    KNOWLEDGE_BASE = (By.XPATH, "//a[@span[text()='Knowledge Base']]")
    CALL_DETAILS_TAB = (By.XPATH, "//a[@automationid='agentCallDetailsTab' and span[text()='Call Details']]")
    CHAT_ICON = (By.XPATH, "//a[@class='btn-internal-chat']")
    PASSWORD = (By.XPATH, "//input[@automationid='enterLoginPassword']")
    AGENT_NAME=(By.XPATH, "//a[@automationid='userNameLink']/span")

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