import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        shop_page = home_page.shopItems()
        action = ActionChains(self.driver)
        action.move_to_element(shop_page.blackberry()).click().perform()
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")

        if shop_page.menu_button().is_displayed():
            shop_page.menu_button().click()
            checkout_page = shop_page.checkout()
        else:
            checkout_page = shop_page.checkout()
        confirm_page = checkout_page.checkout_action()

        confirm_page.country_selector().send_keys('ukr')
        self.wait_until_object_located("CLASS_NAME", "suggestions")
        # <a xpath="1">Ukraine</a>
        confirm_page.choose_country().click()
        confirm_page.mark_checkbox().click()
        confirm_page.choose_purchase_button().click()
        success_test = confirm_page.get_alert_text().text
        log.info("success_test: " + success_test)
        assert "Success! Thank you!" in success_test
        self.driver.get_screenshot_as_file("screen.png")