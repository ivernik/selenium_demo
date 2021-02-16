from selenium.webdriver.common.by import By


class ConfirmPage:
    country = (By.CSS_SELECTOR, "#country")
    country_ukraine = (By.LINK_TEXT, "Ukraine")
    check_box = (By.CSS_SELECTOR, "label[for*='checkbox2']")
    purchase_button =(By.CSS_SELECTOR, ".btn-lg")
    alert_message = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def country_selector(self):
        return self.driver.find_element(*ConfirmPage.country)

    def choose_country(self):
        return self.driver.find_element(*ConfirmPage.country_ukraine)

    def mark_checkbox(self):
        return self.driver.find_element(*ConfirmPage.check_box)

    def choose_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def get_alert_text(self):
        return self.driver.find_element(*ConfirmPage.alert_message)