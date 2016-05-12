from selenium.webdriver.common.by import By


class CommonPageLocators(object):
    NAME_INPUT = (By.NAME, 'name')
    EMAIL_INPUT = (By.NAME, 'email_address')
    PASSWORD_INPUT = (By.NAME, 'password')
    CONTINUE_BUTTON = (By.CLASS_NAME, 'button')
    H1 = (By.TAG_NAME, 'H1')


class TwoFactorPageLocators(object):
    SMS_INPUT = (By.NAME, 'sms_code')


class DashboardPageLocators(object):
    H2 = (By.CLASS_NAME, 'navigation-service-name')
    SMS_TEMPLATES_LINK = (By.LINK_TEXT, 'Text message templates')
    EMAIL_TEMPLATES_LINK = (By.LINK_TEXT, 'Email templates')
    TEAM_MEMBERS_LINK = (By.LINK_TEXT, 'Team members')
    API_KEYS_LINK = (By.LINK_TEXT, 'API keys')


class NavigationLocators(object):
    SIGN_OUT_LINK = (By.LINK_TEXT, 'Sign out')


class UploadCsvLocators(object):
    FILE_INPUT = (By.ID, 'file')
    SEND_BUTTON = (By.CLASS_NAME, 'button')
