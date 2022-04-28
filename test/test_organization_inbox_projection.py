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
from mailslurp_client.models.organization_inbox_projection import OrganizationInboxProjection  # noqa: E501
from mailslurp_client.rest import ApiException

class TestOrganizationInboxProjection(unittest.TestCase):
    """OrganizationInboxProjection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrganizationInboxProjection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.organization_inbox_projection.OrganizationInboxProjection()  # noqa: E501
        if include_optional :
            return OrganizationInboxProjection(
                id = '0', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                name = '0', 
                email_address = '0', 
                favourite = True, 
                tags = [
                    '0'
                    ], 
                team_access = True, 
                inbox_type = 'HTTP_INBOX', 
                read_only = True
            )
        else :
            return OrganizationInboxProjection(
                id = '0',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                favourite = True,
                team_access = True,
                read_only = True,
        )

    def testOrganizationInboxProjection(self):
        """Test OrganizationInboxProjection"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
