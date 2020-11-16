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
from mailslurp_client.api.inbox_controller_api import InboxControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestInboxControllerApi(unittest.TestCase):
    """InboxControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.inbox_controller_api.InboxControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_inbox(self):
        """Test case for create_inbox

        Create an Inbox (email address)  # noqa: E501
        """
        pass

    def test_delete_all_inboxes(self):
        """Test case for delete_all_inboxes

        Delete all inboxes  # noqa: E501
        """
        pass

    def test_delete_inbox(self):
        """Test case for delete_inbox

        Delete inbox  # noqa: E501
        """
        pass

    def test_get_all_inboxes(self):
        """Test case for get_all_inboxes

        List Inboxes Paginated  # noqa: E501
        """
        pass

    def test_get_emails(self):
        """Test case for get_emails

        Get emails in an Inbox  # noqa: E501
        """
        pass

    def test_get_inbox(self):
        """Test case for get_inbox

        Get Inbox  # noqa: E501
        """
        pass

    def test_get_inbox_emails_paginated(self):
        """Test case for get_inbox_emails_paginated

        Get inbox emails paginated  # noqa: E501
        """
        pass

    def test_get_inbox_sent_emails(self):
        """Test case for get_inbox_sent_emails

        Get Inbox Sent Emails  # noqa: E501
        """
        pass

    def test_get_inbox_tags(self):
        """Test case for get_inbox_tags

        Get inbox tags  # noqa: E501
        """
        pass

    def test_get_inboxes(self):
        """Test case for get_inboxes

        List Inboxes / Email Addresses  # noqa: E501
        """
        pass

    def test_send_email(self):
        """Test case for send_email

        Send Email  # noqa: E501
        """
        pass

    def test_set_inbox_favourited(self):
        """Test case for set_inbox_favourited

        Set inbox favourited state  # noqa: E501
        """
        pass

    def test_update_inbox(self):
        """Test case for update_inbox

        Update Inbox  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
