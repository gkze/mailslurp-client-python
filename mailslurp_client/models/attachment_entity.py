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


class AttachmentEntity(object):
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
        'attachment_id': 'str',
        'content_length': 'int',
        'content_type': 'str',
        'created_at': 'datetime',
        'id': 'str',
        'name': 'str',
        'updated_at': 'datetime',
        'user_id': 'str'
    }

    attribute_map = {
        'attachment_id': 'attachmentId',
        'content_length': 'contentLength',
        'content_type': 'contentType',
        'created_at': 'createdAt',
        'id': 'id',
        'name': 'name',
        'updated_at': 'updatedAt',
        'user_id': 'userId'
    }

    def __init__(self, attachment_id=None, content_length=None, content_type=None, created_at=None, id=None, name=None, updated_at=None, user_id=None, local_vars_configuration=None):  # noqa: E501
        """AttachmentEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attachment_id = None
        self._content_length = None
        self._content_type = None
        self._created_at = None
        self._id = None
        self._name = None
        self._updated_at = None
        self._user_id = None
        self.discriminator = None

        self.attachment_id = attachment_id
        if content_length is not None:
            self.content_length = content_length
        if content_type is not None:
            self.content_type = content_type
        self.created_at = created_at
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        self.updated_at = updated_at
        self.user_id = user_id

    @property
    def attachment_id(self):
        """Gets the attachment_id of this AttachmentEntity.  # noqa: E501


        :return: The attachment_id of this AttachmentEntity.  # noqa: E501
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this AttachmentEntity.


        :param attachment_id: The attachment_id of this AttachmentEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and attachment_id is None:  # noqa: E501
            raise ValueError("Invalid value for `attachment_id`, must not be `None`")  # noqa: E501

        self._attachment_id = attachment_id

    @property
    def content_length(self):
        """Gets the content_length of this AttachmentEntity.  # noqa: E501


        :return: The content_length of this AttachmentEntity.  # noqa: E501
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this AttachmentEntity.


        :param content_length: The content_length of this AttachmentEntity.  # noqa: E501
        :type: int
        """

        self._content_length = content_length

    @property
    def content_type(self):
        """Gets the content_type of this AttachmentEntity.  # noqa: E501


        :return: The content_type of this AttachmentEntity.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this AttachmentEntity.


        :param content_type: The content_type of this AttachmentEntity.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def created_at(self):
        """Gets the created_at of this AttachmentEntity.  # noqa: E501


        :return: The created_at of this AttachmentEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AttachmentEntity.


        :param created_at: The created_at of this AttachmentEntity.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this AttachmentEntity.  # noqa: E501


        :return: The id of this AttachmentEntity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AttachmentEntity.


        :param id: The id of this AttachmentEntity.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AttachmentEntity.  # noqa: E501


        :return: The name of this AttachmentEntity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AttachmentEntity.


        :param name: The name of this AttachmentEntity.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def updated_at(self):
        """Gets the updated_at of this AttachmentEntity.  # noqa: E501


        :return: The updated_at of this AttachmentEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AttachmentEntity.


        :param updated_at: The updated_at of this AttachmentEntity.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this AttachmentEntity.  # noqa: E501


        :return: The user_id of this AttachmentEntity.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AttachmentEntity.


        :param user_id: The user_id of this AttachmentEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

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
        if not isinstance(other, AttachmentEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AttachmentEntity):
            return True

        return self.to_dict() != other.to_dict()
