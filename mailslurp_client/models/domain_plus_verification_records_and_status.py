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


class DomainPlusVerificationRecordsAndStatus(object):
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
        'created_at': 'datetime',
        'domain': 'str',
        'id': 'str',
        'updated_at': 'datetime',
        'user_id': 'str',
        'verification_token': 'str',
        'verified': 'bool'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'domain': 'domain',
        'id': 'id',
        'updated_at': 'updatedAt',
        'user_id': 'userId',
        'verification_token': 'verificationToken',
        'verified': 'verified'
    }

    def __init__(self, created_at=None, domain=None, id=None, updated_at=None, user_id=None, verification_token=None, verified=None):  # noqa: E501
        """DomainPlusVerificationRecordsAndStatus - a model defined in OpenAPI"""  # noqa: E501

        self._created_at = None
        self._domain = None
        self._id = None
        self._updated_at = None
        self._user_id = None
        self._verification_token = None
        self._verified = None
        self.discriminator = None

        self.created_at = created_at
        self.domain = domain
        self.id = id
        self.updated_at = updated_at
        self.user_id = user_id
        self.verification_token = verification_token
        self.verified = verified

    @property
    def created_at(self):
        """Gets the created_at of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501


        :return: The created_at of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DomainPlusVerificationRecordsAndStatus.


        :param created_at: The created_at of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def domain(self):
        """Gets the domain of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501


        :return: The domain of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this DomainPlusVerificationRecordsAndStatus.


        :param domain: The domain of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def id(self):
        """Gets the id of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501


        :return: The id of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainPlusVerificationRecordsAndStatus.


        :param id: The id of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def updated_at(self):
        """Gets the updated_at of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501


        :return: The updated_at of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DomainPlusVerificationRecordsAndStatus.


        :param updated_at: The updated_at of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501


        :return: The user_id of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DomainPlusVerificationRecordsAndStatus.


        :param user_id: The user_id of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def verification_token(self):
        """Gets the verification_token of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501


        :return: The verification_token of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :rtype: str
        """
        return self._verification_token

    @verification_token.setter
    def verification_token(self, verification_token):
        """Sets the verification_token of this DomainPlusVerificationRecordsAndStatus.


        :param verification_token: The verification_token of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :type: str
        """
        if verification_token is None:
            raise ValueError("Invalid value for `verification_token`, must not be `None`")  # noqa: E501

        self._verification_token = verification_token

    @property
    def verified(self):
        """Gets the verified of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501


        :return: The verified of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this DomainPlusVerificationRecordsAndStatus.


        :param verified: The verified of this DomainPlusVerificationRecordsAndStatus.  # noqa: E501
        :type: bool
        """
        if verified is None:
            raise ValueError("Invalid value for `verified`, must not be `None`")  # noqa: E501

        self._verified = verified

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
        if not isinstance(other, DomainPlusVerificationRecordsAndStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
