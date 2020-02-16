# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository  ## Basic Concepts  ### Inboxes  Inboxes have real email addresses that can send and receive emails. You can create inboxes with specific email addresses (using custom domains). You can also use randomly assigned MailSlurp addresses as unique, disposable test addresses.   See the InboxController or [inbox and email address guide](https://www.mailslurp.com/guides/) for more information.  ### Receive Emails You can receive emails in a number of ways. You can fetch emails and attachments directly from an inbox. Or you can use `waitFor` endpoints to hold a connection open until an email is received that matches given criteria (such as subject or body content). You can also use webhooks to have emails from multiple inboxes forwarded to your server via HTTP POST.  InboxController methods with `waitFor` in the name have a long timeout period and instruct MailSlurp to wait until an expected email is received. You can set conditions on email counts, subject or body matches, and more.  Most receive methods only return an email ID and not the full email (to keep response sizes low). To fetch the full body or attachments for an email use the email's ID with EmailController endpoints.  See the InboxController or [receiving emails guide](https://www.mailslurp.com/guides/) for more information.  ### Send Emails You can send templated HTML emails in several ways. You must first create an inbox to send an email. An inbox can have a specific address or a randomly assigned one. You can send emails from an inbox using `to`, `cc`, and `bcc` recipient lists or with contacts and contact groups.   Emails can contain plain-text or HTML bodies. You can also use email templates that support [moustache](https://mustache.github.io/) template variables. You can send attachments by first posting files to the AttachmentController and then using the returned IDs in the `attachments` field of the send options.  See the InboxController or [sending emails guide](https://www.mailslurp.com/guides/) for more information.  ### Templates MailSlurp emails support templates. You can create templates in the dashboard or API that contain [moustache](https://mustache.github.io/) style variables: for instance `Hello {{name}}`. Then when sending emails you can pass a map of variables names and values to be used. Additionally, when sending emails with contact groups you can use properties of the contact in your templates like `{{firstName}}` and `{{lastName}}`.  > You can do a lot more with MailSlurp so see the included documentation for more information.    # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class Inbox(object):
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
        'description': 'str',
        'email_address': 'str',
        'expires_at': 'datetime',
        'favourite': 'bool',
        'id': 'str',
        'name': 'str',
        'tags': 'list[str]',
        'user_id': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'description': 'description',
        'email_address': 'emailAddress',
        'expires_at': 'expiresAt',
        'favourite': 'favourite',
        'id': 'id',
        'name': 'name',
        'tags': 'tags',
        'user_id': 'userId'
    }

    def __init__(self, created_at=None, description=None, email_address=None, expires_at=None, favourite=None, id=None, name=None, tags=None, user_id=None, local_vars_configuration=None):  # noqa: E501
        """Inbox - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._description = None
        self._email_address = None
        self._expires_at = None
        self._favourite = None
        self._id = None
        self._name = None
        self._tags = None
        self._user_id = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if email_address is not None:
            self.email_address = email_address
        if expires_at is not None:
            self.expires_at = expires_at
        if favourite is not None:
            self.favourite = favourite
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags
        if user_id is not None:
            self.user_id = user_id

    @property
    def created_at(self):
        """Gets the created_at of this Inbox.  # noqa: E501

        When was the inbox created  # noqa: E501

        :return: The created_at of this Inbox.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Inbox.

        When was the inbox created  # noqa: E501

        :param created_at: The created_at of this Inbox.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this Inbox.  # noqa: E501

        Optional description of an inbox for labelling purposes  # noqa: E501

        :return: The description of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Inbox.

        Optional description of an inbox for labelling purposes  # noqa: E501

        :param description: The description of this Inbox.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email_address(self):
        """Gets the email_address of this Inbox.  # noqa: E501

        The inbox's email address. Send an email to this address and the inbox will receive and store it for you. To retrieve the email use the Inbox and Email Controller endpoints.  # noqa: E501

        :return: The email_address of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this Inbox.

        The inbox's email address. Send an email to this address and the inbox will receive and store it for you. To retrieve the email use the Inbox and Email Controller endpoints.  # noqa: E501

        :param email_address: The email_address of this Inbox.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def expires_at(self):
        """Gets the expires_at of this Inbox.  # noqa: E501

        When, if ever, will the inbox expire and be deleted. If null then this inbox is permanent and the emails in it won't be deleted.  # noqa: E501

        :return: The expires_at of this Inbox.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this Inbox.

        When, if ever, will the inbox expire and be deleted. If null then this inbox is permanent and the emails in it won't be deleted.  # noqa: E501

        :param expires_at: The expires_at of this Inbox.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def favourite(self):
        """Gets the favourite of this Inbox.  # noqa: E501

        Is the inbox favourited  # noqa: E501

        :return: The favourite of this Inbox.  # noqa: E501
        :rtype: bool
        """
        return self._favourite

    @favourite.setter
    def favourite(self, favourite):
        """Sets the favourite of this Inbox.

        Is the inbox favourited  # noqa: E501

        :param favourite: The favourite of this Inbox.  # noqa: E501
        :type: bool
        """

        self._favourite = favourite

    @property
    def id(self):
        """Gets the id of this Inbox.  # noqa: E501

        ID of the inbox  # noqa: E501

        :return: The id of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Inbox.

        ID of the inbox  # noqa: E501

        :param id: The id of this Inbox.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Inbox.  # noqa: E501

        Optional name of the inbox. Displayed in the dashboard for easier search  # noqa: E501

        :return: The name of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Inbox.

        Optional name of the inbox. Displayed in the dashboard for easier search  # noqa: E501

        :param name: The name of this Inbox.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this Inbox.  # noqa: E501

        Tags that inbox has been tagged with  # noqa: E501

        :return: The tags of this Inbox.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Inbox.

        Tags that inbox has been tagged with  # noqa: E501

        :param tags: The tags of this Inbox.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def user_id(self):
        """Gets the user_id of this Inbox.  # noqa: E501

        ID of user that inbox belongs to  # noqa: E501

        :return: The user_id of this Inbox.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Inbox.

        ID of user that inbox belongs to  # noqa: E501

        :param user_id: The user_id of this Inbox.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, Inbox):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Inbox):
            return True

        return self.to_dict() != other.to_dict()
