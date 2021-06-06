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


class ConditionOption(object):
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
        'condition': 'str',
        'value': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'value': 'value'
    }

    def __init__(self, condition=None, value=None, local_vars_configuration=None):  # noqa: E501
        """ConditionOption - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._condition = None
        self._value = None
        self.discriminator = None

        if condition is not None:
            self.condition = condition
        if value is not None:
            self.value = value

    @property
    def condition(self):
        """Gets the condition of this ConditionOption.  # noqa: E501

        The condition to evaluate against the email  # noqa: E501

        :return: The condition of this ConditionOption.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this ConditionOption.

        The condition to evaluate against the email  # noqa: E501

        :param condition: The condition of this ConditionOption.  # noqa: E501
        :type: str
        """
        allowed_values = ["HAS_ATTACHMENTS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and condition not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"  # noqa: E501
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def value(self):
        """Gets the value of this ConditionOption.  # noqa: E501

        What the condition should evaluate to. A string 'TRUE|FALSE' not a boolean.  # noqa: E501

        :return: The value of this ConditionOption.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConditionOption.

        What the condition should evaluate to. A string 'TRUE|FALSE' not a boolean.  # noqa: E501

        :param value: The value of this ConditionOption.  # noqa: E501
        :type: str
        """
        allowed_values = ["TRUE", "FALSE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and value not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `value` ({0}), must be one of {1}"  # noqa: E501
                .format(value, allowed_values)
            )

        self._value = value

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
        if not isinstance(other, ConditionOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConditionOption):
            return True

        return self.to_dict() != other.to_dict()
