from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name_field = (By.CSS_SELECTOR, "input[name='name']")
    email_field = (By.NAME, "email")
    checkbox_ice_cream = (By.ID, "exampleCheck1")
    submit_button = (By.XPATH, "//input[@type='submit']")
    alert_message_css = (By.CSS_SELECTOR, "[class*='alert-success']")
    alert_message_xpath = (By.XPATH, "//*[contains(@class,'alert-success')]")
    alert_message_class_name = (By.CLASS_NAME, "alert-dismissible")
    sex_drop_down = (By.ID, "exampleFormControlSelect1")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        shop_page = ShopPage(self.driver)
        self.driver.find_element(*HomePage.shop).click()
        return shop_page

    def find_name_field(self):
        return self.driver.find_elements(*HomePage.name_field)

    def find_email_field(self):
        return self.driver.find_element(*HomePage.email_field)

    def get_drop_down(self):
        return self.driver.find_element(*HomePage.sex_drop_down)

    def click_on_ckeckbox_ice_cream(self):
        return self.driver.find_element(*HomePage.checkbox_ice_cream).click()

    def click_on_submit_button(self):
        return self.driver.find_element(*HomePage.submit_button).click()

    def text_alert_message_css(self):
        return self.driver.find_element(*HomePage.alert_message_css).text

    def text_alert_message_xpath(self):
        return self.driver.find_element(*HomePage.alert_message_xpath).text

    def text_alert_message_class_name(self):
        return self.driver.find_element(*HomePage.alert_message_class_name).text
