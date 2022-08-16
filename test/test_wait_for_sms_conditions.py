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
import datetime

import mailslurp_client
from mailslurp_client.models.wait_for_sms_conditions import WaitForSmsConditions  # noqa: E501
from mailslurp_client.rest import ApiException

class TestWaitForSmsConditions(unittest.TestCase):
    """WaitForSmsConditions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WaitForSmsConditions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.wait_for_sms_conditions.WaitForSmsConditions()  # noqa: E501
        if include_optional :
            return WaitForSmsConditions(
                phone_number_id = '0', 
                limit = 56, 
                count = 56, 
                delay_timeout = 56, 
                timeout = 56, 
                unread_only = True, 
                count_type = 'EXACTLY', 
                matches = [
                    mailslurp_client.models.sms_match_option.SmsMatchOption(
                        field = 'BODY', 
                        should = 'CONTAIN', 
                        value = '0', )
                    ], 
                sort_direction = 'ASC', 
                since = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return WaitForSmsConditions(
                phone_number_id = '0',
                count = 56,
                timeout = 56,
        )

    def testWaitForSmsConditions(self):
        """Test WaitForSmsConditions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
