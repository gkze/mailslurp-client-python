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
from mailslurp_client.api.template_controller_api import TemplateControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestTemplateControllerApi(unittest.TestCase):
    """TemplateControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.template_controller_api.TemplateControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_template(self):
        """Test case for create_template

        Create a Template  # noqa: E501
        """
        pass

    def test_delete_template(self):
        """Test case for delete_template

        Delete Template  # noqa: E501
        """
        pass

    def test_get_all_templates(self):
        """Test case for get_all_templates

        Get all Templates in paginated format  # noqa: E501
        """
        pass

    def test_get_template(self):
        """Test case for get_template

        Get Template  # noqa: E501
        """
        pass

    def test_get_templates(self):
        """Test case for get_templates

        Get all Templates  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
