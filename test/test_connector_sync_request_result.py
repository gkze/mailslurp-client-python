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
from mailslurp_client.models.connector_sync_request_result import ConnectorSyncRequestResult  # noqa: E501
from mailslurp_client.rest import ApiException

class TestConnectorSyncRequestResult(unittest.TestCase):
    """ConnectorSyncRequestResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ConnectorSyncRequestResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.connector_sync_request_result.ConnectorSyncRequestResult()  # noqa: E501
        if include_optional :
            return ConnectorSyncRequestResult(
                sync_result = mailslurp_client.models.connector_sync_result.ConnectorSyncResult(
                    email_sync_count = 56, 
                    log_lines = [
                        '0'
                        ], ), 
                exception = mailslurp_client.models.connector_sync_request_result_exception.ConnectorSyncRequestResult_exception(
                    cause = mailslurp_client.models.connector_sync_request_result_exception_cause.ConnectorSyncRequestResult_exception_cause(
                        stack_trace = [
                            mailslurp_client.models.connector_sync_request_result_exception_cause_stack_trace.ConnectorSyncRequestResult_exception_cause_stackTrace(
                                class_loader_name = '0', 
                                module_name = '0', 
                                module_version = '0', 
                                method_name = '0', 
                                file_name = '0', 
                                line_number = 56, 
                                native_method = True, 
                                class_name = '0', )
                            ], 
                        message = '0', 
                        suppressed = [
                            mailslurp_client.models.connector_sync_request_result_exception_cause_suppressed.ConnectorSyncRequestResult_exception_cause_suppressed(
                                message = '0', 
                                localized_message = '0', )
                            ], 
                        localized_message = '0', ), 
                    stack_trace = [
                        mailslurp_client.models.connector_sync_request_result_exception_cause_stack_trace.ConnectorSyncRequestResult_exception_cause_stackTrace(
                            class_loader_name = '0', 
                            module_name = '0', 
                            module_version = '0', 
                            method_name = '0', 
                            file_name = '0', 
                            line_number = 56, 
                            native_method = True, 
                            class_name = '0', )
                        ], 
                    message = '0', 
                    suppressed = [
                        mailslurp_client.models.connector_sync_request_result_exception_cause_suppressed.ConnectorSyncRequestResult_exception_cause_suppressed(
                            message = '0', 
                            localized_message = '0', )
                        ], 
                    localized_message = '0', ), 
                event_id = '0'
            )
        else :
            return ConnectorSyncRequestResult(
        )

    def testConnectorSyncRequestResult(self):
        """Test ConnectorSyncRequestResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
