from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    checkout = (By.CSS_SELECTOR, ".btn-success")

    def __init__(self, driver):
        self.driver = driver

    def checkout_action(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
