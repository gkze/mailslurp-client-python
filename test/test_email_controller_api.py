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
from mailslurp_client.api.email_controller_api import EmailControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestEmailControllerApi(unittest.TestCase):
    """EmailControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.email_controller_api.EmailControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_all_emails(self):
        """Test case for delete_all_emails

        Delete all emails in all inboxes.  # noqa: E501
        """
        pass

    def test_delete_email(self):
        """Test case for delete_email

        Delete an email  # noqa: E501
        """
        pass

    def test_download_attachment(self):
        """Test case for download_attachment

        Get email attachment bytes. Returned as `octet-stream` with content type header. If you have trouble with byte responses try the `downloadAttachmentBase64` response endpoints and convert the base 64 encoded content to a file or string.  # noqa: E501
        """
        pass

    def test_download_attachment_base64(self):
        """Test case for download_attachment_base64

        Get email attachment as base64 encoded string as an alternative to binary responses. Decode the `base64FileContents` as a `utf-8` encoded string or array of bytes depending on the `contentType`.  # noqa: E501
        """
        pass

    def test_download_body(self):
        """Test case for download_body

        Get email body as string. Returned as `plain/text` with content type header.  # noqa: E501
        """
        pass

    def test_download_body_bytes(self):
        """Test case for download_body_bytes

        Get email body in bytes. Returned as `octet-stream` with content type header.  # noqa: E501
        """
        pass

    def test_forward_email(self):
        """Test case for forward_email

        Forward email to recipients  # noqa: E501
        """
        pass

    def test_get_attachment_meta_data(self):
        """Test case for get_attachment_meta_data

        Get email attachment metadata. This is the `contentType` and `contentLength` of an attachment. To get the individual attachments  use the `downloadAttachment` methods.  # noqa: E501
        """
        pass

    def test_get_attachments1(self):
        """Test case for get_attachments1

        Get all email attachment metadata. Metadata includes name and size of attachments.  # noqa: E501
        """
        pass

    def test_get_email(self):
        """Test case for get_email

        Get email content including headers and body. Expects email to exist by ID. For emails that may not have arrived yet use the WaitForController.  # noqa: E501
        """
        pass

    def test_get_email_content_match(self):
        """Test case for get_email_content_match

        Get email content regex pattern match results. Runs regex against email body and returns match groups.  # noqa: E501
        """
        pass

    def test_get_email_html(self):
        """Test case for get_email_html

        Get email content as HTML. For displaying emails in browser context.  # noqa: E501
        """
        pass

    def test_get_email_html_query(self):
        """Test case for get_email_html_query

        Parse and return text from an email, stripping HTML and decoding encoded characters  # noqa: E501
        """
        pass

    def test_get_email_text_lines(self):
        """Test case for get_email_text_lines

        Parse and return text from an email, stripping HTML and decoding encoded characters  # noqa: E501
        """
        pass

    def test_get_emails_paginated(self):
        """Test case for get_emails_paginated

        Get all emails in all inboxes in paginated form. Email API list all.  # noqa: E501
        """
        pass

    def test_get_latest_email(self):
        """Test case for get_latest_email

        Get latest email in all inboxes. Most recently received.  # noqa: E501
        """
        pass

    def test_get_latest_email_in_inbox(self):
        """Test case for get_latest_email_in_inbox

        Get latest email in an inbox. Use `WaitForController` to get emails that may not have arrived yet.  # noqa: E501
        """
        pass

    def test_get_organization_emails_paginated(self):
        """Test case for get_organization_emails_paginated

        Get all organization emails. List team or shared test email accounts  # noqa: E501
        """
        pass

    def test_get_raw_email_contents(self):
        """Test case for get_raw_email_contents

        Get raw email string. Returns unparsed raw SMTP message with headers and body.  # noqa: E501
        """
        pass

    def test_get_raw_email_json(self):
        """Test case for get_raw_email_json

        Get raw email in JSON. Unparsed SMTP message in JSON wrapper format.  # noqa: E501
        """
        pass

    def test_get_unread_email_count(self):
        """Test case for get_unread_email_count

        Get unread email count  # noqa: E501
        """
        pass

    def test_reply_to_email(self):
        """Test case for reply_to_email

        Reply to an email  # noqa: E501
        """
        pass

    def test_validate_email(self):
        """Test case for validate_email

        Validate email HTML contents  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
