from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import pytest
# pytest.set_trace()


# @pytest.mark.usefixtures("setup")
class TestHomePage(BaseClass):

    def test_home_page(self, get_data):
        home_page = HomePage(self.driver)
        name_field = home_page.find_name_field()
        name_field[0].send_keys(get_data["firstName"])
        pytest.set_trace()
        home_page.find_email_field().send_keys(get_data["email"])
        self.select_option_by_text(home_page.get_drop_down(), get_data["gender"])
        home_page.click_on_ckeckbox_ice_cream()

        # driver.find_element_by_css_selector("input[value='Submit']").click()
        home_page.click_on_submit_button()
        # REG ex for CSS
        print(home_page.text_alert_message_css())
        # REG ex for Xpath
        print(home_page.text_alert_message_xpath(), "number 1 ")
        message = home_page.text_alert_message_class_name()
        print(message)

        assert "Success! The Form has been submitted successfully!." in message
        self.driver.refresh()
        #driver.close()

    @pytest.fixture(params=HomePageData.test_homePage_data)
    def get_data(self, request):
        return request.param
