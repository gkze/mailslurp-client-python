# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mailslurp_client
from mailslurp_client.api.sms_controller_api import SmsControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestSmsControllerApi(unittest.TestCase):
    """SmsControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.sms_controller_api.SmsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_sms_message(self):
        """Test case for delete_sms_message

        Delete SMS message.  # noqa: E501
        """
        pass

    def test_delete_sms_messages(self):
        """Test case for delete_sms_messages

        Delete all SMS messages  # noqa: E501
        """
        pass

    def test_get_sms_message(self):
        """Test case for get_sms_message

        Get SMS content including body. Expects SMS to exist by ID. For SMS that may not have arrived yet use the WaitForController.  # noqa: E501
        """
        pass

    def test_get_sms_messages_paginated(self):
        """Test case for get_sms_messages_paginated

        Get all SMS messages in all phone numbers in paginated form. .  # noqa: E501
        """
        pass

    def test_get_unread_sms_count(self):
        """Test case for get_unread_sms_count

        Get unread SMS count  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
