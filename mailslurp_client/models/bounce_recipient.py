# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class BounceRecipient(object):
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
        'id': 'str',
        'user_id': 'str',
        'recipient': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'recipient': 'recipient',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, id=None, user_id=None, recipient=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """BounceRecipient - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user_id = None
        self._recipient = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if recipient is not None:
            self.recipient = recipient
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this BounceRecipient.  # noqa: E501


        :return: The id of this BounceRecipient.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BounceRecipient.


        :param id: The id of this BounceRecipient.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this BounceRecipient.  # noqa: E501


        :return: The user_id of this BounceRecipient.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BounceRecipient.


        :param user_id: The user_id of this BounceRecipient.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def recipient(self):
        """Gets the recipient of this BounceRecipient.  # noqa: E501


        :return: The recipient of this BounceRecipient.  # noqa: E501
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this BounceRecipient.


        :param recipient: The recipient of this BounceRecipient.  # noqa: E501
        :type: str
        """

        self._recipient = recipient

    @property
    def created_at(self):
        """Gets the created_at of this BounceRecipient.  # noqa: E501


        :return: The created_at of this BounceRecipient.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BounceRecipient.


        :param created_at: The created_at of this BounceRecipient.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this BounceRecipient.  # noqa: E501


        :return: The updated_at of this BounceRecipient.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BounceRecipient.


        :param updated_at: The updated_at of this BounceRecipient.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, BounceRecipient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BounceRecipient):
            return True

        return self.to_dict() != other.to_dict()
