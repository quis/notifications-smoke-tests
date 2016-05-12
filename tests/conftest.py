import pytest

from selenium import webdriver

from tests.pages.rollups import sign_in
from config import Config


@pytest.fixture(scope="session")
def profile():
    return {'name': Config.FUNCTIONAL_TEST_NAME,
            'email': Config.FUNCTIONAL_TEST_EMAIL,
            'service_name': Config.FUNCTIONAL_TEST_SERVICE_NAME,
            'password': Config.FUNCTIONAL_TEST_PASSWORD,
            'mobile': Config.TWILIO_TEST_NUMBER,
            'service_id': Config.SERVICE_ID,
            'email_template_id': Config.EMAIL_TEMPLATE_ID,
            'sms_template_id': Config.SMS_TEMPLATE_ID,
            'config': Config}


@pytest.fixture(scope="module")
def driver(request):
    driver = webdriver.Firefox()

    def clear_up():
        driver.delete_all_cookies()
        driver.close()

    request.addfinalizer(clear_up)
    return driver


@pytest.fixture(scope="session")
def base_url():
    return Config.NOTIFY_ADMIN_URL


@pytest.fixture(scope="module")
def login_user(driver, profile):
    sign_in(driver, profile)
