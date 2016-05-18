import os


class Config(object):
    ENVIRONMENT = os.environ['ENVIRONMENT']
    NOTIFY_ADMIN_URL = os.environ['live_NOTIFY_ADMIN_URL']
    NOTIFY_API_URL = os.environ['live_NOTIFY_API_URL']
    TWILIO_TEST_NUMBER = os.environ['live_TWILIO_TEST_NUMBER']
    TWILIO_ACCOUNT_SID = os.environ['live_TWILIO_ACCOUNT_SID']
    TWILIO_AUTH_TOKEN = os.environ['live_TWILIO_AUTH_TOKEN']
    FUNCTIONAL_TEST_NAME = os.environ['live_FUNCTIONAL_TEST_NAME']
    FUNCTIONAL_TEST_EMAIL = os.environ['live_FUNCTIONAL_TEST_EMAIL']
    FUNCTIONAL_TEST_PASSWORD = os.environ['live_FUNCTIONAL_TEST_PASSWORD']
    SMS_TEMPLATE_ID = os.environ['live_SMS_TEMPLATE_ID']
    EMAIL_TEMPLATE_ID = os.environ['live_EMAIL_TEMPLATE_ID']
    FUNCTIONAL_TEST_SERVICE_NAME = os.environ['live_FUNCTIONAL_TEST_SERVICE_NAME']
    SERVICE_ID = os.environ['live_SERVICE_ID']
    API_KEY = os.environ['live_API_KEY']
    EMAIL_NOTIFICATION_LABEL = 'notify'
    EMAIL_TRIES = 10
    EMAIL_DELAY = 5
    DESKPRO_API_HOST = os.environ['live_DESKPRO_API_HOST']
    DESKPRO_API_KEY = os.environ['live_DESKPRO_API_KEY']
    DESKPRO_PERSON_EMAIL = os.environ['live_DESKPRO_PERSON_EMAIL']
    DESKPRO_TEAM_ID = os.environ['live_DESKPRO_TEAM_ID']
    DESKPRO_DEPT_ID = os.environ['live_DESKPRO_DEPT_ID']
    DESKPRO_ASSIGNED_AGENT_TEAM_ID = os.environ['live_DESKPRO_ASSIGNED_AGENT_TEAM_ID']
