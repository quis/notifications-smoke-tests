import os
import shutil

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import Config

from tests.pages.element import (
    EmailInputElement,
    PasswordInputElement,
    SmsInputElement,
    FileInputElement
)


from tests.pages.locators import (
    CommonPageLocators,
    DashboardPageLocators,
    NavigationLocators,
    UploadCsvLocators
)


class BasePage(object):

    base_url = Config.NOTIFY_ADMIN_URL
    sign_out_link = NavigationLocators.SIGN_OUT_LINK

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def sign_out(self):
        # getting and clicking on sign out link not working on travis
        self.driver.get(self.base_url+'/sign-out')


class SignInPage(BasePage):

    email_input = EmailInputElement()
    password_input = PasswordInputElement()
    continue_button = CommonPageLocators.CONTINUE_BUTTON

    def get(self):
        self.driver.get(self.base_url+'/sign-in')

    def is_current(self):
        return self.driver.current_url == self.base_url+'/sign-in'

    def is_currect(self):
        return self.driver.current_url == self.base_url+'/sign-in'

    def fill_login_form(self, email, password):
        self.email_input = email
        self.password_input = password

    def click_continue_button(self):
        element = self.wait_for_element(SignInPage.continue_button)
        element.click()

    def login(self, email, password):
        self.fill_login_form(email, password)
        self.click_continue_button()


class VerifyPage(BasePage):

    sms_input = SmsInputElement()
    continue_button = CommonPageLocators.CONTINUE_BUTTON

    def is_current(self):
        return self.driver.current_url == self.base_url+'/verify'

    def click_continue_button(self):
        element = self.wait_for_element(VerifyPage.continue_button)
        element.click()

    def verify(self, code):
        self.sms_input = code
        self.click_continue_button()


class TwoFactorPage(BasePage):

    sms_input = SmsInputElement()
    continue_button = CommonPageLocators.CONTINUE_BUTTON

    def is_current(self):
        return self.driver.current_url == self.base_url+'/two-factor'

    def click_continue_button(self):
        element = self.wait_for_element(TwoFactorPage.continue_button)
        element.click()

    def verify(self, code):
        self.sms_input = code
        self.click_continue_button()


class DashboardPage(BasePage):

    h2 = DashboardPageLocators.H2
    sms_templates_link = DashboardPageLocators.SMS_TEMPLATES_LINK
    email_templates_link = DashboardPageLocators.EMAIL_TEMPLATES_LINK
    team_members_link = DashboardPageLocators.TEAM_MEMBERS_LINK
    api_keys_link = DashboardPageLocators.API_KEYS_LINK

    def is_current(self, service_id):
        expected = '{}/services/{}/dashboard'.format(self.base_url, service_id)
        return self.driver.current_url == expected

    def h2_is_service_name(self, expected_name):
        element = self.wait_for_element(DashboardPage.h2)
        return expected_name == element.text

    def click_sms_templates(self):
        element = self.wait_for_element(DashboardPage.sms_templates_link)
        element.click()

    def click_email_templates(self):
        element = self.wait_for_element(DashboardPage.email_templates_link)
        element.click()

    def click_team_members_link(self):
        element = self.wait_for_element(DashboardPage.team_members_link)
        element.click()

    def click_user_profile_link(self, link_text):
        element = self.wait_for_element((By.LINK_TEXT, link_text))
        element.click()

    def click_api_keys_link(self):
        element = self.wait_for_element(DashboardPage.api_keys_link)
        element.click()

    def get_service_id(self):
        return self.driver.current_url.split('/services/')[1].split('/')[0]

    def go_to_dashboard_for_service(self, service_id):
        url = "{}/services/{}/dashboard".format(self.base_url, service_id)
        self.driver.get(url)


class UploadCsvPage(BasePage):

    file_input_element = FileInputElement()
    send_button = UploadCsvLocators.SEND_BUTTON

    def click_send(self):
        element = self.wait_for_element(UploadCsvPage.send_button)
        element.click()

    def upload_csv(self, directory, path):
        file_path = os.path.join(directory, 'sample.csv')
        self.file_input_element = file_path
        self.click_send()
        shutil.rmtree(directory, ignore_errors=True)

    def go_to_upload_csv_for_service_and_template(self, service_id, template_id):
        url = "{}/services/{}/send/{}/csv".format(self.base_url, service_id, template_id)
        self.driver.get(url)
