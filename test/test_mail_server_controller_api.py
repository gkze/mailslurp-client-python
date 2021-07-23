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
from mailslurp_client.api.mail_server_controller_api import MailServerControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestMailServerControllerApi(unittest.TestCase):
    """MailServerControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.mail_server_controller_api.MailServerControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_describe_mail_server_domain(self):
        """Test case for describe_mail_server_domain

        Get DNS Mail Server records for a domain  # noqa: E501
        """
        pass

    def test_get_dns_lookup(self):
        """Test case for get_dns_lookup

        Lookup DNS records for a domain  # noqa: E501
        """
        pass

    def test_get_ip_address(self):
        """Test case for get_ip_address

        Get IP address for a domain  # noqa: E501
        """
        pass

    def test_verify_email_address(self):
        """Test case for verify_email_address

        Verify the existence of an email address at a given mail server.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
