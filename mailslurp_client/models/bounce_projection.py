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


class BounceProjection(object):
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
        'subject': 'str',
        'sender': 'str',
        'created_at': 'datetime',
        'bounce_type': 'str',
        'bounce_mta': 'str'
    }

    attribute_map = {
        'id': 'id',
        'subject': 'subject',
        'sender': 'sender',
        'created_at': 'createdAt',
        'bounce_type': 'bounceType',
        'bounce_mta': 'bounceMta'
    }

    def __init__(self, id=None, subject=None, sender=None, created_at=None, bounce_type=None, bounce_mta=None, local_vars_configuration=None):  # noqa: E501
        """BounceProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._subject = None
        self._sender = None
        self._created_at = None
        self._bounce_type = None
        self._bounce_mta = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if subject is not None:
            self.subject = subject
        self.sender = sender
        self.created_at = created_at
        if bounce_type is not None:
            self.bounce_type = bounce_type
        if bounce_mta is not None:
            self.bounce_mta = bounce_mta

    @property
    def id(self):
        """Gets the id of this BounceProjection.  # noqa: E501


        :return: The id of this BounceProjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BounceProjection.


        :param id: The id of this BounceProjection.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def subject(self):
        """Gets the subject of this BounceProjection.  # noqa: E501


        :return: The subject of this BounceProjection.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this BounceProjection.


        :param subject: The subject of this BounceProjection.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def sender(self):
        """Gets the sender of this BounceProjection.  # noqa: E501


        :return: The sender of this BounceProjection.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this BounceProjection.


        :param sender: The sender of this BounceProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sender is None:  # noqa: E501
            raise ValueError("Invalid value for `sender`, must not be `None`")  # noqa: E501

        self._sender = sender

    @property
    def created_at(self):
        """Gets the created_at of this BounceProjection.  # noqa: E501


        :return: The created_at of this BounceProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BounceProjection.


        :param created_at: The created_at of this BounceProjection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def bounce_type(self):
        """Gets the bounce_type of this BounceProjection.  # noqa: E501


        :return: The bounce_type of this BounceProjection.  # noqa: E501
        :rtype: str
        """
        return self._bounce_type

    @bounce_type.setter
    def bounce_type(self, bounce_type):
        """Sets the bounce_type of this BounceProjection.


        :param bounce_type: The bounce_type of this BounceProjection.  # noqa: E501
        :type: str
        """

        self._bounce_type = bounce_type

    @property
    def bounce_mta(self):
        """Gets the bounce_mta of this BounceProjection.  # noqa: E501


        :return: The bounce_mta of this BounceProjection.  # noqa: E501
        :rtype: str
        """
        return self._bounce_mta

    @bounce_mta.setter
    def bounce_mta(self, bounce_mta):
        """Sets the bounce_mta of this BounceProjection.


        :param bounce_mta: The bounce_mta of this BounceProjection.  # noqa: E501
        :type: str
        """

        self._bounce_mta = bounce_mta

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
        if not isinstance(other, BounceProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BounceProjection):
            return True

        return self.to_dict() != other.to_dict()
