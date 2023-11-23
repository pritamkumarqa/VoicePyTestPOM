from typing import Optional, Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging

logging.basicConfig(level=logging.ERROR)
class BasePage:
    WAIT_TIME = 20  # Set a constant for wait time

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        try:
            element = WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.element_to_be_clickable(by_locator)
            )
            element.click()
        except TimeoutException:
            logging.error(f"Element with locator {by_locator} not clickable within {self.WAIT_TIME} seconds")

    def do_send_keys(self, by_locator, text):
        try:
            element = WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.visibility_of_element_located(by_locator)
            )
            element.send_keys(text)
        except TimeoutException:
            logging.error(f"Element with locator {by_locator} not visible within {self.WAIT_TIME} seconds")

    def get_element_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.visibility_of_element_located(by_locator)
            )
            return element.text
        except TimeoutException:
            logging.error(f"Element with locator {by_locator} not visible within {self.WAIT_TIME} seconds")
            return None

    def is_visible(self, by_locator):
        try:
            WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.visibility_of_element_located(by_locator)
            )
            return True
        except TimeoutException:
            logging.error(f"Element with locator {by_locator} not visible within {self.WAIT_TIME} seconds")
            return False

    def get_title(self, title):
        try:
            WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.title_is(title)
            )
            return self.driver.title
        except TimeoutException:
            logging.error(f"Title {title} not found within {self.WAIT_TIME} seconds")
            return None

    def clear_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.visibility_of_element_located(by_locator)
            )
            element.clear()
        except TimeoutException:
            logging.error(f"Element with locator {by_locator} not visible within {self.WAIT_TIME} seconds")

    def is_element_present(self, by_locator):
        try:
            WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.presence_of_element_located(by_locator)
            )
            return True
        except TimeoutException:
            logging.error(f"Element with locator {by_locator} not present within {self.WAIT_TIME} seconds")
            return False

    def is_element_enabled(self, by_locator):
        try:
            element = WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.visibility_of_element_located(by_locator)
            )
            return element.is_enabled()
        except TimeoutException:
            logging.error(f"Element with locator {by_locator} not visible within {self.WAIT_TIME} seconds")
            return False

    def switch_to_frame(self, by_locator):
        try:
            frame = WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.frame_to_be_available_and_switch_to_it(by_locator)
            )
            return frame
        except TimeoutException:
            logging.error(f"Frame with locator {by_locator} not available within {self.WAIT_TIME} seconds")
            return None

    def select_item_from_dropdown_list(self, by_locator, item_text):
        item_locator = None
        try:
            # Wait for the dropdown items to be visible
            WebDriverWait(self.driver, self.WAIT_TIME).until(EC.visibility_of_element_located(by_locator))
            xpath = by_locator[1]

            # Find and click the desired item
            item_xpath = f"{xpath}[text()='{item_text}']"
            item_locator = (By.XPATH, item_xpath)
            print(item_locator)
            element = WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.element_to_be_clickable(item_locator)
            )
            element.click()
        except TimeoutException:
            logging.error(f"Element with locator {item_locator} not visible within {self.WAIT_TIME} seconds")
            print("I am exception here for", item_text)


