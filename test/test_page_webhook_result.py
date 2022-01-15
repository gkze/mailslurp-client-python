# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mailslurp_client
from mailslurp_client.models.page_webhook_result import PageWebhookResult  # noqa: E501
from mailslurp_client.rest import ApiException

class TestPageWebhookResult(unittest.TestCase):
    """PageWebhookResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PageWebhookResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.page_webhook_result.PageWebhookResult()  # noqa: E501
        if include_optional :
            return PageWebhookResult(
                content = [
                    mailslurp_client.models.webhook_result_dto.WebhookResultDto(
                        id = '0', 
                        user_id = '0', 
                        inbox_id = '0', 
                        webhook_id = '0', 
                        webhook_url = '0', 
                        message_id = '0', 
                        redrive_id = '0', 
                        http_method = 'GET', 
                        webhook_event = 'EMAIL_RECEIVED', 
                        response_status = 56, 
                        response_time_millis = 56, 
                        response_body_extract = '0', 
                        result_type = 'BAD_RESPONSE', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        seen = True, )
                    ], 
                pageable = mailslurp_client.models.pageable_object.PageableObject(
                    offset = 56, 
                    sort = mailslurp_client.models.sort.Sort(
                        empty = True, 
                        sorted = True, 
                        unsorted = True, ), 
                    page_number = 56, 
                    page_size = 56, 
                    paged = True, 
                    unpaged = True, ), 
                total = 56, 
                last = True, 
                total_elements = 56, 
                total_pages = 56, 
                size = 56, 
                number = 56, 
                sort = mailslurp_client.models.sort.Sort(
                    empty = True, 
                    sorted = True, 
                    unsorted = True, ), 
                first = True, 
                number_of_elements = 56, 
                empty = True
            )
        else :
            return PageWebhookResult(
        )

    def testPageWebhookResult(self):
        """Test PageWebhookResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
