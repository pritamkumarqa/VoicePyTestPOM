from selenium.webdriver.common.by import By


class LoginPageElements:

    '''By Locaotrs OR XPath'''
    USERNAME = (By.XPATH, "//input[@automationid='enterLoginUsername']")
    PASSWORD = (By.XPATH, "//input[@automationid='enterLoginPassword']")
    LOGIN_BUTTON = (By.XPATH, "//button[@automationid='loginButton']")
    GOOGLE_SSO_BUTTON = (By.XPATH, "//button[@automationid='googlePlusLoginLoginBtn']")
    SAML_SSO_BUTTON = (By.XPATH, "//button[@automationid='SAMLLoginBtn']")
    FORCE_LOGIN_PAGE_HEADING = (By.XPATH, "//h2[@automationid='confirmationModalTitle' and text()='Force Login']")
    LOGIN_ERROR_MSG = (By.XPATH, "//span[contains(@class,'error-msg text-error') and text()='UserId or Password is either incorrect or left blank']")
    WORKMODE_PAGE_HEADING = (By.XPATH, "//h2[text()='Working Mode Selection']")
    FORCE_LOGIN_OK_BUTTON = (By.XPATH, "//button[@automationid='confirmationBtn1']")
    CAMPAIGN_SELECT_PAGE = (By.XPATH, "//h2[@automationid='campaignSelectionHeader']")
    VOICE_CAMPAIGN_INPUT = (By.XPATH, "//input[@type='search' and @placeholder='Select Voice Campaign']")
    VOICE_CAMPAIGN_LIST = (By.XPATH, "//li[@role='treeitem']")
    CAMPAIGN_SELECT_NEXT_BUTTON = (By.XPATH, "//button[@automationid='camapignSaveBtn' and span[text()='Next']]")
    WORK_MODE = (By.XPATH, "//input[@type='radio' and @name='workingMode']/following-sibling::label")
    #WORK_MODE = (By.XPATH, "//span[input[@type='radio' and @name='workingMode']]/label")
    WORK_MODE_SELECT_NEXT_BUTTON = (By.XPATH, "//button[span[text()='Next']]")
    EXTENSION_SELECT_PAGE = (By.XPATH, "//h2[@automationid='extensionSelectionHeader']")
    EXTENSION_SEARCH = (By.XPATH, "//div[@automationid='extensionSelectionList']//span[@title='Select Extension']")
    EXTENSION_LIST = (By.XPATH, "//span[input[@type='search']]/following-sibling::span/ul[@role='tree']/li[@role='treeitem']")
    EXTENSION_PHONE_INPUT = (By.XPATH, "//input[@placeholder='Enter Number']")
    EXTENSION_SELECT_DONE_BUTTON = (By.XPATH, "//button[@automationid='extensionSaveBtn']")
    AGENT_PREFRENCE_DROPDOWN = (By.XPATH, "//a[@automationid='userNameLink']")
    SUPERVISOR_PREFRENCE_DROPDOWN = (By.XPATH, "//a[@automationid='supervisorPreferenceContainer']")
    LOGOUT_BUTTON = (By.XPATH, "//a[span[text()='Logout']]")
