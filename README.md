[![Build Status](https://travis-ci.org/alphagov/notifications-smoke-tests.svg)](https://travis-ci.org/alphagov/notifications-smoke-tests)

# notifications-smoke-tests
Smoke tests for Notification applications


## This repo contains some basic smoke tests of the following

- Sign in to live admin notify application
- Send an sms notification from an uploaded csv file
- Send an email notification from an uploaded csv file
- Send an sms message using the [notify python client library](https://github.com/alphagov/notifications-python-client) to send via the notify api
- Send an email message using the [notify python client library](https://github.com/alphagov/notifications-python-client) to send via the notify api

### These test run on travis and the following environment variables are set on the build settings page:
```
ENVIRONMENT=live
live_FUNCTIONAL_TEST_NAME
live_FUNCTIONAL_TEST_SERVICE_NAME
live_TWILIO_ACCOUNT_SID
live_TWILIO_AUTH_TOKEN
live_TWILIO_TEST_NUMBER
live_FUNCTIONAL_TEST_EMAIL
live_FUNCTIONAL_TEST_PASSWORD
live_NOTIFY_ADMIN_URL
live_NOTIFY_API_URL
live_SMS_TEMPLATE_ID
live_EMAIL_TEMPLATE_ID
live_SERVICE_ID
live_API_KEY
live_DESKPRO_PERSON_EMAIL
live_DESKPRO_TEAM_ID
live_DESKPRO_API_HOST
live_DESKPRO_API_KEY
```

The test suite is run every 10 minutes on Travis and is invoked by [a scheduled job](https://github.com/alphagov/notifications-functional-tests/blob/master/smoke_tester.py) that runs on a Heroku instance.

You can run this suite locally by creating an environment.sh with the above set to correct values. Then run:

```
./scripts/run_smoke_tests.sh
```


