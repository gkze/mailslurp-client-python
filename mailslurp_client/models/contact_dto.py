# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Overview  #### Inboxes  Inboxes have real email addresses that can send and receive emails. You can create inboxes with specific email addresses (using custom domains). You can also use randomly assigned MailSlurp addresses as unique, disposable test addresses.   See the InboxController or [inbox and email address guide](https://www.mailslurp.com/guides/) for more information.  #### Receive Emails You can receive emails in a number of ways. You can fetch emails and attachments directly from an inbox. Or you can use `waitFor` endpoints to hold a connection open until an email is received that matches given criteria (such as subject or body content). You can also use webhooks to have emails from multiple inboxes forwarded to your server via HTTP POST.  InboxController methods with `waitFor` in the name have a long timeout period and instruct MailSlurp to wait until an expected email is received. You can set conditions on email counts, subject or body matches, and more.  Most receive methods only return an email ID and not the full email (to keep response sizes low). To fetch the full body or attachments for an email use the email's ID with EmailController endpoints.  See the InboxController or [receiving emails guide](https://www.mailslurp.com/guides/) for more information.  #### Send Emails You can send templated HTML emails in several ways. You must first create an inbox to send an email. An inbox can have a specific address or a randomly assigned one. You can send emails from an inbox using `to`, `cc`, and `bcc` recipient lists or with contacts and contact groups.   Emails can contain plain-text or HTML bodies. You can also use email templates that support [moustache](https://mustache.github.io/) template variables. You can send attachments by first posting files to the AttachmentController and then using the returned IDs in the `attachments` field of the send options.  See the InboxController or [sending emails guide](https://www.mailslurp.com/guides/) for more information.  ## Templates MailSlurp emails support templates. You can create templates in the dashboard or API that contain [moustache](https://mustache.github.io/) style variables: for instance `Hello {{name}}`. Then when sending emails you can pass a map of variables names and values to be used. Additionally, when sending emails with contact groups you can use properties of the contact in your templates like `{{firstName}}` and `{{lastName}}``.  ## Explore       # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class ContactDto(object):
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
        'company': 'str',
        'email_addresses': 'list[str]',
        'first_name': 'str',
        'id': 'str',
        'last_name': 'str',
        'meta_data': 'JsonNode',
        'opt_out': 'bool',
        'tags': 'list[str]'
    }

    attribute_map = {
        'company': 'company',
        'email_addresses': 'emailAddresses',
        'first_name': 'firstName',
        'id': 'id',
        'last_name': 'lastName',
        'meta_data': 'metaData',
        'opt_out': 'optOut',
        'tags': 'tags'
    }

    def __init__(self, company=None, email_addresses=None, first_name=None, id=None, last_name=None, meta_data=None, opt_out=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """ContactDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._company = None
        self._email_addresses = None
        self._first_name = None
        self._id = None
        self._last_name = None
        self._meta_data = None
        self._opt_out = None
        self._tags = None
        self.discriminator = None

        if company is not None:
            self.company = company
        self.email_addresses = email_addresses
        if first_name is not None:
            self.first_name = first_name
        self.id = id
        if last_name is not None:
            self.last_name = last_name
        if meta_data is not None:
            self.meta_data = meta_data
        if opt_out is not None:
            self.opt_out = opt_out
        self.tags = tags

    @property
    def company(self):
        """Gets the company of this ContactDto.  # noqa: E501


        :return: The company of this ContactDto.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ContactDto.


        :param company: The company of this ContactDto.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def email_addresses(self):
        """Gets the email_addresses of this ContactDto.  # noqa: E501


        :return: The email_addresses of this ContactDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_addresses

    @email_addresses.setter
    def email_addresses(self, email_addresses):
        """Sets the email_addresses of this ContactDto.


        :param email_addresses: The email_addresses of this ContactDto.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and email_addresses is None:  # noqa: E501
            raise ValueError("Invalid value for `email_addresses`, must not be `None`")  # noqa: E501

        self._email_addresses = email_addresses

    @property
    def first_name(self):
        """Gets the first_name of this ContactDto.  # noqa: E501


        :return: The first_name of this ContactDto.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ContactDto.


        :param first_name: The first_name of this ContactDto.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def id(self):
        """Gets the id of this ContactDto.  # noqa: E501


        :return: The id of this ContactDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContactDto.


        :param id: The id of this ContactDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def last_name(self):
        """Gets the last_name of this ContactDto.  # noqa: E501


        :return: The last_name of this ContactDto.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ContactDto.


        :param last_name: The last_name of this ContactDto.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def meta_data(self):
        """Gets the meta_data of this ContactDto.  # noqa: E501


        :return: The meta_data of this ContactDto.  # noqa: E501
        :rtype: JsonNode
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ContactDto.


        :param meta_data: The meta_data of this ContactDto.  # noqa: E501
        :type: JsonNode
        """

        self._meta_data = meta_data

    @property
    def opt_out(self):
        """Gets the opt_out of this ContactDto.  # noqa: E501


        :return: The opt_out of this ContactDto.  # noqa: E501
        :rtype: bool
        """
        return self._opt_out

    @opt_out.setter
    def opt_out(self, opt_out):
        """Sets the opt_out of this ContactDto.


        :param opt_out: The opt_out of this ContactDto.  # noqa: E501
        :type: bool
        """

        self._opt_out = opt_out

    @property
    def tags(self):
        """Gets the tags of this ContactDto.  # noqa: E501


        :return: The tags of this ContactDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ContactDto.


        :param tags: The tags of this ContactDto.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

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
        if not isinstance(other, ContactDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContactDto):
            return True

        return self.to_dict() != other.to_dict()
