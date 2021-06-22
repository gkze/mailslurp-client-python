# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class BulkSendEmailOptions(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'inbox_ids': 'list[str]',
        'send_email_options': 'SendEmailOptions'
    }

    attribute_map = {
        'inbox_ids': 'inboxIds',
        'send_email_options': 'sendEmailOptions'
    }

    def __init__(self, inbox_ids=None, send_email_options=None, local_vars_configuration=None):  # noqa: E501
        """BulkSendEmailOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._inbox_ids = None
        self._send_email_options = None
        self.discriminator = None

        if inbox_ids is not None:
            self.inbox_ids = inbox_ids
        if send_email_options is not None:
            self.send_email_options = send_email_options

    @property
    def inbox_ids(self):
        """Gets the inbox_ids of this BulkSendEmailOptions.  # noqa: E501

        Inboxes to send the email from  # noqa: E501

        :return: The inbox_ids of this BulkSendEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._inbox_ids

    @inbox_ids.setter
    def inbox_ids(self, inbox_ids):
        """Sets the inbox_ids of this BulkSendEmailOptions.

        Inboxes to send the email from  # noqa: E501

        :param inbox_ids: The inbox_ids of this BulkSendEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._inbox_ids = inbox_ids

    @property
    def send_email_options(self):
        """Gets the send_email_options of this BulkSendEmailOptions.  # noqa: E501


        :return: The send_email_options of this BulkSendEmailOptions.  # noqa: E501
        :rtype: SendEmailOptions
        """
        return self._send_email_options

    @send_email_options.setter
    def send_email_options(self, send_email_options):
        """Sets the send_email_options of this BulkSendEmailOptions.


        :param send_email_options: The send_email_options of this BulkSendEmailOptions.  # noqa: E501
        :type: SendEmailOptions
        """

        self._send_email_options = send_email_options

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BulkSendEmailOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkSendEmailOptions):
            return True

        return self.to_dict() != other.to_dict()
