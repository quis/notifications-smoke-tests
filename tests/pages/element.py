from selenium.webdriver.support.ui import WebDriverWait

from tests.pages.locators import (
    CommonPageLocators,
    TwoFactorPageLocators,
    UploadCsvLocators,
)


class BasePageElement(object):

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")


class EmailInputElement(BasePageElement):
    locator = CommonPageLocators.EMAIL_INPUT[1]


class PasswordInputElement(BasePageElement):
    locator = CommonPageLocators.PASSWORD_INPUT[1]


class SmsInputElement(BasePageElement):
    locator = TwoFactorPageLocators.SMS_INPUT[1]


class FileInputElement(BasePageElement):
    locator = UploadCsvLocators.FILE_INPUT[1]
