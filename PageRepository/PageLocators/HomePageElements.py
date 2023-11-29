from selenium.webdriver.common.by import By


class HomePageElements:

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
