# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class AttachmentMetaData(object):
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
        'content_length': 'int',
        'content_type': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'content_length': 'contentLength',
        'content_type': 'contentType',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, content_length=None, content_type=None, id=None, name=None, local_vars_configuration=None):  # noqa: E501
        """AttachmentMetaData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content_length = None
        self._content_type = None
        self._id = None
        self._name = None
        self.discriminator = None

        if content_length is not None:
            self.content_length = content_length
        if content_type is not None:
            self.content_type = content_type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def content_length(self):
        """Gets the content_length of this AttachmentMetaData.  # noqa: E501

        Size of attachment in bytes  # noqa: E501

        :return: The content_length of this AttachmentMetaData.  # noqa: E501
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this AttachmentMetaData.

        Size of attachment in bytes  # noqa: E501

        :param content_length: The content_length of this AttachmentMetaData.  # noqa: E501
        :type: int
        """

        self._content_length = content_length

    @property
    def content_type(self):
        """Gets the content_type of this AttachmentMetaData.  # noqa: E501

        Content type of attachment  # noqa: E501

        :return: The content_type of this AttachmentMetaData.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this AttachmentMetaData.

        Content type of attachment  # noqa: E501

        :param content_type: The content_type of this AttachmentMetaData.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def id(self):
        """Gets the id of this AttachmentMetaData.  # noqa: E501

        ID of attachment  # noqa: E501

        :return: The id of this AttachmentMetaData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AttachmentMetaData.

        ID of attachment  # noqa: E501

        :param id: The id of this AttachmentMetaData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AttachmentMetaData.  # noqa: E501

        Name of attachment  # noqa: E501

        :return: The name of this AttachmentMetaData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AttachmentMetaData.

        Name of attachment  # noqa: E501

        :param name: The name of this AttachmentMetaData.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, AttachmentMetaData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachmentMetaData):
            return True

        return self.to_dict() != other.to_dict()
