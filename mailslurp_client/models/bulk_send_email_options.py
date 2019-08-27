# coding: utf-8

"""
    MailSlurp API

    For documentation see [developer guide](https://www.mailslurp.com/developers). [Create an account](https://app.mailslurp.com) in the MailSlurp Dashboard to [view your API Key](https://app). For all bugs, feature requests, or help please [see support](https://www.mailslurp.com/support/).  # noqa: E501

    OpenAPI spec version: 0.0.1-alpha
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


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

    def __init__(self, inbox_ids=None, send_email_options=None):  # noqa: E501
        """BulkSendEmailOptions - a model defined in OpenAPI"""  # noqa: E501

        self._inbox_ids = None
        self._send_email_options = None
        self.discriminator = None

        self.inbox_ids = inbox_ids
        self.send_email_options = send_email_options

    @property
    def inbox_ids(self):
        """Gets the inbox_ids of this BulkSendEmailOptions.  # noqa: E501


        :return: The inbox_ids of this BulkSendEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._inbox_ids

    @inbox_ids.setter
    def inbox_ids(self, inbox_ids):
        """Sets the inbox_ids of this BulkSendEmailOptions.


        :param inbox_ids: The inbox_ids of this BulkSendEmailOptions.  # noqa: E501
        :type: list[str]
        """
        if inbox_ids is None:
            raise ValueError("Invalid value for `inbox_ids`, must not be `None`")  # noqa: E501

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
        if send_email_options is None:
            raise ValueError("Invalid value for `send_email_options`, must not be `None`")  # noqa: E501

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

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
