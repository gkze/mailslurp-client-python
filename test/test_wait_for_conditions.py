# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: beb7302db3b2458f4bba957b81a42c95e2289b11
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mailslurp_client
from mailslurp_client.models.wait_for_conditions import WaitForConditions  # noqa: E501
from mailslurp_client.rest import ApiException

class TestWaitForConditions(unittest.TestCase):
    """WaitForConditions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WaitForConditions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.wait_for_conditions.WaitForConditions()  # noqa: E501
        if include_optional :
            return WaitForConditions(
                count = 56, 
                count_type = 'EXACTLY', 
                inbox_id = '0', 
                matches = [
                    mailslurp_client.models.match_option.MatchOption(
                        field = 'SUBJECT', 
                        should = 'CONTAIN', 
                        value = '0', )
                    ], 
                sort_direction = 'ASC', 
                timeout = 56, 
                unread_only = True
            )
        else :
            return WaitForConditions(
        )

    def testWaitForConditions(self):
        """Test WaitForConditions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
