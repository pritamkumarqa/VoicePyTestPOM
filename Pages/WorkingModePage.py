from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class WorkingModePage(BasePage):

    '''By Locaotrs OR XPath'''

    WORK_MODE = (By.XPATH, "//input[@type='radio' and @name='workingMode']/following-sibling::label")
    #WORK_MODE = (By.XPATH, "//span[input[@type='radio' and @name='workingMode']]/label")
    WORK_MODE_SELECT_NEXT_BUTTON = (By.XPATH, "//button[span[text()='Next']]")

    '''Constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)

    ''' Page Actions for Login Page '''

    def do_work_mode_select(self, user_working_mode):
        self.select_item_from_dropdown_list(self.WORK_MODE,user_working_mode)
        self.do_click(self.WORK_MODE_SELECT_NEXT_BUTTON)
