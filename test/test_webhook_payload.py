# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mailslurp_client
from mailslurp_client.models.webhook_payload import WebhookPayload  # noqa: E501
from mailslurp_client.rest import ApiException

class TestWebhookPayload(unittest.TestCase):
    """WebhookPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WebhookPayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.webhook_payload.WebhookPayload()  # noqa: E501
        if include_optional :
            return WebhookPayload(
                attachment_meta_datas = [
                    mailslurp_client.models.attachment_meta_data.AttachmentMetaData(
                        content_length = 56, 
                        content_type = '0', 
                        id = '0', 
                        name = '0', )
                    ], 
                bcc = [
                    '0'
                    ], 
                cc = [
                    '0'
                    ], 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                email_id = '0', 
                event_name = 'EMAIL_RECEIVED', 
                _from = '0', 
                inbox_id = '0', 
                message_id = '0', 
                subject = '0', 
                to = [
                    '0'
                    ], 
                webhook_id = '0', 
                webhook_name = '0'
            )
        else :
            return WebhookPayload(
        )

    def testWebhookPayload(self):
        """Test WebhookPayload"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
