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


class TemplateDto(object):
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
        'name': 'str',
        'variables': 'list[TemplateVariable]',
        'content': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'variables': 'variables',
        'content': 'content',
        'created_at': 'createdAt'
    }

    def __init__(self, id=None, name=None, variables=None, content=None, created_at=None, local_vars_configuration=None):  # noqa: E501
        """TemplateDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._variables = None
        self._content = None
        self._created_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.variables = variables
        self.content = content
        self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this TemplateDto.  # noqa: E501

        ID of template  # noqa: E501

        :return: The id of this TemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateDto.

        ID of template  # noqa: E501

        :param id: The id of this TemplateDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this TemplateDto.  # noqa: E501

        Template name  # noqa: E501

        :return: The name of this TemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateDto.

        Template name  # noqa: E501

        :param name: The name of this TemplateDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def variables(self):
        """Gets the variables of this TemplateDto.  # noqa: E501

        Variables available in template that can be replaced with values  # noqa: E501

        :return: The variables of this TemplateDto.  # noqa: E501
        :rtype: list[TemplateVariable]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this TemplateDto.

        Variables available in template that can be replaced with values  # noqa: E501

        :param variables: The variables of this TemplateDto.  # noqa: E501
        :type: list[TemplateVariable]
        """
        if self.local_vars_configuration.client_side_validation and variables is None:  # noqa: E501
            raise ValueError("Invalid value for `variables`, must not be `None`")  # noqa: E501

        self._variables = variables

    @property
    def content(self):
        """Gets the content of this TemplateDto.  # noqa: E501

        Content of the template  # noqa: E501

        :return: The content of this TemplateDto.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this TemplateDto.

        Content of the template  # noqa: E501

        :param content: The content of this TemplateDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def created_at(self):
        """Gets the created_at of this TemplateDto.  # noqa: E501

        Created at time  # noqa: E501

        :return: The created_at of this TemplateDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TemplateDto.

        Created at time  # noqa: E501

        :param created_at: The created_at of this TemplateDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

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
        if not isinstance(other, TemplateDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateDto):
            return True

        return self.to_dict() != other.to_dict()
