# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class OrganizationInboxProjection(object):
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
        'created_at': 'datetime',
        'name': 'str',
        'email_address': 'str',
        'favourite': 'bool',
        'tags': 'list[str]',
        'team_access': 'bool',
        'inbox_type': 'str',
        'read_only': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'createdAt',
        'name': 'name',
        'email_address': 'emailAddress',
        'favourite': 'favourite',
        'tags': 'tags',
        'team_access': 'teamAccess',
        'inbox_type': 'inboxType',
        'read_only': 'readOnly'
    }

    def __init__(self, id=None, created_at=None, name=None, email_address=None, favourite=None, tags=None, team_access=None, inbox_type=None, read_only=None, local_vars_configuration=None):  # noqa: E501
        """OrganizationInboxProjection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_at = None
        self._name = None
        self._email_address = None
        self._favourite = None
        self._tags = None
        self._team_access = None
        self._inbox_type = None
        self._read_only = None
        self.discriminator = None

        self.id = id
        self.created_at = created_at
        if name is not None:
            self.name = name
        if email_address is not None:
            self.email_address = email_address
        self.favourite = favourite
        if tags is not None:
            self.tags = tags
        self.team_access = team_access
        if inbox_type is not None:
            self.inbox_type = inbox_type
        self.read_only = read_only

    @property
    def id(self):
        """Gets the id of this OrganizationInboxProjection.  # noqa: E501

        ID of the inbox. The ID is a UUID-V4 format string. Use the inboxId for calls to Inbox and Email Controller endpoints. See the emailAddress property for the email address or the inbox. To get emails in an inbox use the WaitFor and Inbox Controller methods `waitForLatestEmail` and `getEmails` methods respectively. Inboxes can be used with aliases to forward emails automatically.  # noqa: E501

        :return: The id of this OrganizationInboxProjection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationInboxProjection.

        ID of the inbox. The ID is a UUID-V4 format string. Use the inboxId for calls to Inbox and Email Controller endpoints. See the emailAddress property for the email address or the inbox. To get emails in an inbox use the WaitFor and Inbox Controller methods `waitForLatestEmail` and `getEmails` methods respectively. Inboxes can be used with aliases to forward emails automatically.  # noqa: E501

        :param id: The id of this OrganizationInboxProjection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this OrganizationInboxProjection.  # noqa: E501

        When the inbox was created. Time stamps are in ISO DateTime Format `yyyy-MM-dd'T'HH:mm:ss.SSSXXX` e.g. `2000-10-31T01:30:00.000-05:00`.  # noqa: E501

        :return: The created_at of this OrganizationInboxProjection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OrganizationInboxProjection.

        When the inbox was created. Time stamps are in ISO DateTime Format `yyyy-MM-dd'T'HH:mm:ss.SSSXXX` e.g. `2000-10-31T01:30:00.000-05:00`.  # noqa: E501

        :param created_at: The created_at of this OrganizationInboxProjection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this OrganizationInboxProjection.  # noqa: E501

        Name of the inbox and used as the sender name when sending emails .Displayed in the dashboard for easier search  # noqa: E501

        :return: The name of this OrganizationInboxProjection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationInboxProjection.

        Name of the inbox and used as the sender name when sending emails .Displayed in the dashboard for easier search  # noqa: E501

        :param name: The name of this OrganizationInboxProjection.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email_address(self):
        """Gets the email_address of this OrganizationInboxProjection.  # noqa: E501

        The inbox's email address. Inbox projections and previews may not include the email address. To view the email address fetch the inbox entity directly. Send an email to this address and the inbox will receive and store it for you. Note the email address in MailSlurp match characters exactly and are case sensitive so `+123` additions are considered different addresses. To retrieve the email use the Inbox and Email Controller endpoints with the inbox ID.  # noqa: E501

        :return: The email_address of this OrganizationInboxProjection.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this OrganizationInboxProjection.

        The inbox's email address. Inbox projections and previews may not include the email address. To view the email address fetch the inbox entity directly. Send an email to this address and the inbox will receive and store it for you. Note the email address in MailSlurp match characters exactly and are case sensitive so `+123` additions are considered different addresses. To retrieve the email use the Inbox and Email Controller endpoints with the inbox ID.  # noqa: E501

        :param email_address: The email_address of this OrganizationInboxProjection.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def favourite(self):
        """Gets the favourite of this OrganizationInboxProjection.  # noqa: E501

        Is the inbox a favorite inbox. Make an inbox a favorite is typically done in the dashboard for quick access or filtering  # noqa: E501

        :return: The favourite of this OrganizationInboxProjection.  # noqa: E501
        :rtype: bool
        """
        return self._favourite

    @favourite.setter
    def favourite(self, favourite):
        """Sets the favourite of this OrganizationInboxProjection.

        Is the inbox a favorite inbox. Make an inbox a favorite is typically done in the dashboard for quick access or filtering  # noqa: E501

        :param favourite: The favourite of this OrganizationInboxProjection.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and favourite is None:  # noqa: E501
            raise ValueError("Invalid value for `favourite`, must not be `None`")  # noqa: E501

        self._favourite = favourite

    @property
    def tags(self):
        """Gets the tags of this OrganizationInboxProjection.  # noqa: E501

        Tags that inbox has been tagged with. Tags can be added to inboxes to group different inboxes within an account. You can also search for inboxes by tag in the dashboard UI.  # noqa: E501

        :return: The tags of this OrganizationInboxProjection.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this OrganizationInboxProjection.

        Tags that inbox has been tagged with. Tags can be added to inboxes to group different inboxes within an account. You can also search for inboxes by tag in the dashboard UI.  # noqa: E501

        :param tags: The tags of this OrganizationInboxProjection.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def team_access(self):
        """Gets the team_access of this OrganizationInboxProjection.  # noqa: E501

        Does inbox permit team access for organization team members. If so team users can use inbox and emails associated with it. See the team access guide at https://www.mailslurp.com/guides/team-email-account-sharing/  # noqa: E501

        :return: The team_access of this OrganizationInboxProjection.  # noqa: E501
        :rtype: bool
        """
        return self._team_access

    @team_access.setter
    def team_access(self, team_access):
        """Sets the team_access of this OrganizationInboxProjection.

        Does inbox permit team access for organization team members. If so team users can use inbox and emails associated with it. See the team access guide at https://www.mailslurp.com/guides/team-email-account-sharing/  # noqa: E501

        :param team_access: The team_access of this OrganizationInboxProjection.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and team_access is None:  # noqa: E501
            raise ValueError("Invalid value for `team_access`, must not be `None`")  # noqa: E501

        self._team_access = team_access

    @property
    def inbox_type(self):
        """Gets the inbox_type of this OrganizationInboxProjection.  # noqa: E501

        Type of inbox. HTTP inboxes are faster and better for most cases. SMTP inboxes are more suited for public facing inbound messages (but cannot send).  # noqa: E501

        :return: The inbox_type of this OrganizationInboxProjection.  # noqa: E501
        :rtype: str
        """
        return self._inbox_type

    @inbox_type.setter
    def inbox_type(self, inbox_type):
        """Sets the inbox_type of this OrganizationInboxProjection.

        Type of inbox. HTTP inboxes are faster and better for most cases. SMTP inboxes are more suited for public facing inbound messages (but cannot send).  # noqa: E501

        :param inbox_type: The inbox_type of this OrganizationInboxProjection.  # noqa: E501
        :type: str
        """
        allowed_values = ["HTTP_INBOX", "SMTP_INBOX"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and inbox_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `inbox_type` ({0}), must be one of {1}"  # noqa: E501
                .format(inbox_type, allowed_values)
            )

        self._inbox_type = inbox_type

    @property
    def read_only(self):
        """Gets the read_only of this OrganizationInboxProjection.  # noqa: E501

        Is the inbox readOnly for the caller. Read only means can not be deleted or modified. This flag is present when using team accounts and shared inboxes.  # noqa: E501

        :return: The read_only of this OrganizationInboxProjection.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this OrganizationInboxProjection.

        Is the inbox readOnly for the caller. Read only means can not be deleted or modified. This flag is present when using team accounts and shared inboxes.  # noqa: E501

        :param read_only: The read_only of this OrganizationInboxProjection.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and read_only is None:  # noqa: E501
            raise ValueError("Invalid value for `read_only`, must not be `None`")  # noqa: E501

        self._read_only = read_only

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
        if not isinstance(other, OrganizationInboxProjection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrganizationInboxProjection):
            return True

        return self.to_dict() != other.to_dict()
