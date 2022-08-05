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
from mailslurp_client.api.tracking_controller_api import TrackingControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestTrackingControllerApi(unittest.TestCase):
    """TrackingControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.tracking_controller_api.TrackingControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tracking_pixel(self):
        """Test case for create_tracking_pixel

        Create tracking pixel  # noqa: E501
        """
        pass

    def test_get_all_tracking_pixels(self):
        """Test case for get_all_tracking_pixels

        Get tracking pixels  # noqa: E501
        """
        pass

    def test_get_tracking_pixel(self):
        """Test case for get_tracking_pixel

        Get pixel  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
