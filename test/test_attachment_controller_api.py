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
from mailslurp_client.api.attachment_controller_api import AttachmentControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestAttachmentControllerApi(unittest.TestCase):
    """AttachmentControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.attachment_controller_api.AttachmentControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_upload_attachment(self):
        """Test case for upload_attachment

        Upload an attachment for sending  # noqa: E501
        """
        pass

    def test_upload_multipart_form(self):
        """Test case for upload_multipart_form

        Upload an attachment for sending using Multipart Form  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
