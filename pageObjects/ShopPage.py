from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class ShopPage:
    blackberry_device = (By.XPATH, "//a[text()='Blackberry']/../following::div/button")
    burger_button = (By.CSS_SELECTOR, "span.navbar-toggler-icon")
    checkout_button = (By.CSS_SELECTOR, ".btn-primary")

    def __init__(self, driver):
        self.driver = driver

    def blackberry(self):
        return self.driver.find_element(*ShopPage.blackberry_device)

    def menu_button(self):
        return self.driver.find_element(*ShopPage.burger_button)

    def checkout(self):
        self.driver.find_element(*ShopPage.checkout_button).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
