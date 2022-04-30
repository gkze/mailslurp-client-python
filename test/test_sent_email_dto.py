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
from mailslurp_client.models.sent_email_dto import SentEmailDto  # noqa: E501
from mailslurp_client.rest import ApiException

class TestSentEmailDto(unittest.TestCase):
    """SentEmailDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SentEmailDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.sent_email_dto.SentEmailDto()  # noqa: E501
        if include_optional :
            return SentEmailDto(
                id = '0', 
                user_id = '0', 
                inbox_id = '0', 
                to = [
                    '0'
                    ], 
                _from = '0', 
                reply_to = '0', 
                cc = [
                    '0'
                    ], 
                bcc = [
                    '0'
                    ], 
                attachments = [
                    '0'
                    ], 
                subject = '0', 
                body_md5_hash = '0', 
                body = '0', 
                charset = '0', 
                is_html = True, 
                sent_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                pixel_ids = [
                    '0'
                    ], 
                message_id = '0'
            )
        else :
            return SentEmailDto(
                id = '0',
                user_id = '0',
                inbox_id = '0',
                sent_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testSentEmailDto(self):
        """Test SentEmailDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
