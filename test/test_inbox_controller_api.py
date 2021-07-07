# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

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

        Create an inbox email address. An inbox has a real email address and can send and receive emails. Inboxes can be either `SMTP` or `HTTP` inboxes.  # noqa: E501
        """
        pass

    def test_create_inbox_ruleset(self):
        """Test case for create_inbox_ruleset

        Create an inbox ruleset  # noqa: E501
        """
        pass

    def test_create_inbox_with_defaults(self):
        """Test case for create_inbox_with_defaults

        Create an inbox with default options. Uses MailSlurp domain pool address and is private.  # noqa: E501
        """
        pass

    def test_create_inbox_with_options(self):
        """Test case for create_inbox_with_options

        Create an inbox with options. Extended options for inbox creation.  # noqa: E501
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

        List All Inboxes Paginated  # noqa: E501
        """
        pass

    def test_get_emails(self):
        """Test case for get_emails

        Get emails in an Inbox. This method is not idempotent as it allows retries and waits if you want certain conditions to be met before returning. For simple listing and sorting of known emails use the email controller instead.  # noqa: E501
        """
        pass

    def test_get_inbox(self):
        """Test case for get_inbox

        Get Inbox. Returns properties of an inbox.  # noqa: E501
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

        List Inboxes and email addresses  # noqa: E501
        """
        pass

    def test_get_organization_inboxes(self):
        """Test case for get_organization_inboxes

        List Organization Inboxes Paginated  # noqa: E501
        """
        pass

    def test_list_inbox_rulesets(self):
        """Test case for list_inbox_rulesets

        List inbox rulesets  # noqa: E501
        """
        pass

    def test_list_inbox_tracking_pixels(self):
        """Test case for list_inbox_tracking_pixels

        List inbox tracking pixels  # noqa: E501
        """
        pass

    def test_send_email(self):
        """Test case for send_email

        Send Email  # noqa: E501
        """
        pass

    def test_send_email_and_confirm(self):
        """Test case for send_email_and_confirm

        Send email and return sent confirmation  # noqa: E501
        """
        pass

    def test_send_test_email(self):
        """Test case for send_test_email

        Send a test email to inbox  # noqa: E501
        """
        pass

    def test_set_inbox_favourited(self):
        """Test case for set_inbox_favourited

        Set inbox favourited state  # noqa: E501
        """
        pass

    def test_update_inbox(self):
        """Test case for update_inbox

        Update Inbox. Change name and description. Email address is not editable.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
