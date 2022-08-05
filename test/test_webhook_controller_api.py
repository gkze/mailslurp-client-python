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
from mailslurp_client.api.webhook_controller_api import WebhookControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestWebhookControllerApi(unittest.TestCase):
    """WebhookControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.webhook_controller_api.WebhookControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_account_webhook(self):
        """Test case for create_account_webhook

        Attach a WebHook URL to an inbox  # noqa: E501
        """
        pass

    def test_create_webhook(self):
        """Test case for create_webhook

        Attach a WebHook URL to an inbox  # noqa: E501
        """
        pass

    def test_create_webhook_for_phone_number(self):
        """Test case for create_webhook_for_phone_number

        Attach a WebHook URL to a phone number  # noqa: E501
        """
        pass

    def test_delete_all_webhooks(self):
        """Test case for delete_all_webhooks

        Delete all webhooks  # noqa: E501
        """
        pass

    def test_delete_webhook(self):
        """Test case for delete_webhook

        Delete and disable a Webhook for an Inbox  # noqa: E501
        """
        pass

    def test_delete_webhook_by_id(self):
        """Test case for delete_webhook_by_id

        Delete a webhook  # noqa: E501
        """
        pass

    def test_get_all_webhook_results(self):
        """Test case for get_all_webhook_results

        Get results for all webhooks  # noqa: E501
        """
        pass

    def test_get_all_webhooks(self):
        """Test case for get_all_webhooks

        List Webhooks Paginated  # noqa: E501
        """
        pass

    def test_get_inbox_webhooks_paginated(self):
        """Test case for get_inbox_webhooks_paginated

        Get paginated webhooks for an Inbox  # noqa: E501
        """
        pass

    def test_get_json_schema_for_webhook_event(self):
        """Test case for get_json_schema_for_webhook_event

        """
        pass

    def test_get_json_schema_for_webhook_payload(self):
        """Test case for get_json_schema_for_webhook_payload

        """
        pass

    def test_get_test_webhook_payload(self):
        """Test case for get_test_webhook_payload

        """
        pass

    def test_get_test_webhook_payload_bounce(self):
        """Test case for get_test_webhook_payload_bounce

        """
        pass

    def test_get_test_webhook_payload_bounce_recipient(self):
        """Test case for get_test_webhook_payload_bounce_recipient

        """
        pass

    def test_get_test_webhook_payload_email_opened(self):
        """Test case for get_test_webhook_payload_email_opened

        """
        pass

    def test_get_test_webhook_payload_email_read(self):
        """Test case for get_test_webhook_payload_email_read

        """
        pass

    def test_get_test_webhook_payload_for_webhook(self):
        """Test case for get_test_webhook_payload_for_webhook

        """
        pass

    def test_get_test_webhook_payload_new_attachment(self):
        """Test case for get_test_webhook_payload_new_attachment

        Get webhook test payload for new attachment event  # noqa: E501
        """
        pass

    def test_get_test_webhook_payload_new_contact(self):
        """Test case for get_test_webhook_payload_new_contact

        Get webhook test payload for new contact event  # noqa: E501
        """
        pass

    def test_get_test_webhook_payload_new_email(self):
        """Test case for get_test_webhook_payload_new_email

        Get webhook test payload for new email event  # noqa: E501
        """
        pass

    def test_get_webhook(self):
        """Test case for get_webhook

        Get a webhook  # noqa: E501
        """
        pass

    def test_get_webhook_result(self):
        """Test case for get_webhook_result

        Get a webhook result for a webhook  # noqa: E501
        """
        pass

    def test_get_webhook_results(self):
        """Test case for get_webhook_results

        Get a webhook results for a webhook  # noqa: E501
        """
        pass

    def test_get_webhook_results_unseen_error_count(self):
        """Test case for get_webhook_results_unseen_error_count

        Get count of unseen webhook results with error status  # noqa: E501
        """
        pass

    def test_get_webhooks(self):
        """Test case for get_webhooks

        Get all webhooks for an Inbox  # noqa: E501
        """
        pass

    def test_redrive_webhook_result(self):
        """Test case for redrive_webhook_result

        Get a webhook result and try to resend the original webhook payload  # noqa: E501
        """
        pass

    def test_send_test_data(self):
        """Test case for send_test_data

        Send webhook test data  # noqa: E501
        """
        pass

    def test_update_webhook_headers(self):
        """Test case for update_webhook_headers

        Update a webhook request headers  # noqa: E501
        """
        pass

    def test_verify_webhook_signature(self):
        """Test case for verify_webhook_signature

        Verify a webhook payload signature  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
