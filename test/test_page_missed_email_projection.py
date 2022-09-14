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
from mailslurp_client.models.page_missed_email_projection import PageMissedEmailProjection  # noqa: E501
from mailslurp_client.rest import ApiException

class TestPageMissedEmailProjection(unittest.TestCase):
    """PageMissedEmailProjection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PageMissedEmailProjection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.page_missed_email_projection.PageMissedEmailProjection()  # noqa: E501
        if include_optional :
            return PageMissedEmailProjection(
                content = [
                    mailslurp_client.models.missed_email_projection.MissedEmailProjection(
                        id = '0', 
                        from = '0', 
                        subject = '0', 
                        user_id = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
                pageable = mailslurp_client.models.pageable_object.PageableObject(
                    offset = 56, 
                    sort = mailslurp_client.models.sort.Sort(
                        empty = True, 
                        sorted = True, 
                        unsorted = True, ), 
                    paged = True, 
                    unpaged = True, 
                    page_number = 56, 
                    page_size = 56, ), 
                total = 56, 
                total_elements = 56, 
                total_pages = 56, 
                last = True, 
                size = 56, 
                number = 56, 
                sort = mailslurp_client.models.sort.Sort(
                    empty = True, 
                    sorted = True, 
                    unsorted = True, ), 
                number_of_elements = 56, 
                first = True, 
                empty = True
            )
        else :
            return PageMissedEmailProjection(
        )

    def testPageMissedEmailProjection(self):
        """Test PageMissedEmailProjection"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
