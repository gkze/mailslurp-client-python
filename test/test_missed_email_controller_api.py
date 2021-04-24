# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mailslurp_client
from mailslurp_client.api.missed_email_controller_api import MissedEmailControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestMissedEmailControllerApi(unittest.TestCase):
    """MissedEmailControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.missed_email_controller_api.MissedEmailControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_missed_emails(self):
        """Test case for get_all_missed_emails

        Get all MissedEmails in paginated format  # noqa: E501
        """
        pass

    def test_get_missed_email(self):
        """Test case for get_missed_email

        Get MissedEmail  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
