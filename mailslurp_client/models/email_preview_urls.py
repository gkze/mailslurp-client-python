# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class EmailPreviewUrls(object):
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
        'raw_smtp_message_url': 'str',
        'plain_html_body_url': 'str'
    }

    attribute_map = {
        'raw_smtp_message_url': 'rawSmtpMessageUrl',
        'plain_html_body_url': 'plainHtmlBodyUrl'
    }

    def __init__(self, raw_smtp_message_url=None, plain_html_body_url=None, local_vars_configuration=None):  # noqa: E501
        """EmailPreviewUrls - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._raw_smtp_message_url = None
        self._plain_html_body_url = None
        self.discriminator = None

        self.raw_smtp_message_url = raw_smtp_message_url
        self.plain_html_body_url = plain_html_body_url

    @property
    def raw_smtp_message_url(self):
        """Gets the raw_smtp_message_url of this EmailPreviewUrls.  # noqa: E501


        :return: The raw_smtp_message_url of this EmailPreviewUrls.  # noqa: E501
        :rtype: str
        """
        return self._raw_smtp_message_url

    @raw_smtp_message_url.setter
    def raw_smtp_message_url(self, raw_smtp_message_url):
        """Sets the raw_smtp_message_url of this EmailPreviewUrls.


        :param raw_smtp_message_url: The raw_smtp_message_url of this EmailPreviewUrls.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and raw_smtp_message_url is None:  # noqa: E501
            raise ValueError("Invalid value for `raw_smtp_message_url`, must not be `None`")  # noqa: E501

        self._raw_smtp_message_url = raw_smtp_message_url

    @property
    def plain_html_body_url(self):
        """Gets the plain_html_body_url of this EmailPreviewUrls.  # noqa: E501


        :return: The plain_html_body_url of this EmailPreviewUrls.  # noqa: E501
        :rtype: str
        """
        return self._plain_html_body_url

    @plain_html_body_url.setter
    def plain_html_body_url(self, plain_html_body_url):
        """Sets the plain_html_body_url of this EmailPreviewUrls.


        :param plain_html_body_url: The plain_html_body_url of this EmailPreviewUrls.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and plain_html_body_url is None:  # noqa: E501
            raise ValueError("Invalid value for `plain_html_body_url`, must not be `None`")  # noqa: E501

        self._plain_html_body_url = plain_html_body_url

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
        if not isinstance(other, EmailPreviewUrls):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailPreviewUrls):
            return True

        return self.to_dict() != other.to_dict()
