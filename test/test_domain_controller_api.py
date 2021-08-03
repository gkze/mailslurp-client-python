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
from mailslurp_client.api.domain_controller_api import DomainControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestDomainControllerApi(unittest.TestCase):
    """DomainControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.domain_controller_api.DomainControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_domain_wildcard_catch_all(self):
        """Test case for add_domain_wildcard_catch_all

        Add catch all wild card inbox to domain  # noqa: E501
        """
        pass

    def test_create_domain(self):
        """Test case for create_domain

        Create Domain  # noqa: E501
        """
        pass

    def test_delete_domain(self):
        """Test case for delete_domain

        Delete a domain  # noqa: E501
        """
        pass

    def test_get_domain(self):
        """Test case for get_domain

        Get a domain  # noqa: E501
        """
        pass

    def test_get_domains(self):
        """Test case for get_domains

        Get domains  # noqa: E501
        """
        pass

    def test_update_domain(self):
        """Test case for update_domain

        Update a domain  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
