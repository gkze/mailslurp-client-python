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


class ForwardEmailOptions(object):
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
        'to': 'list[str]',
        'subject': 'str',
        'cc': 'list[str]',
        'bcc': 'list[str]'
    }

    attribute_map = {
        'to': 'to',
        'subject': 'subject',
        'cc': 'cc',
        'bcc': 'bcc'
    }

    def __init__(self, to=None, subject=None, cc=None, bcc=None, local_vars_configuration=None):  # noqa: E501
        """ForwardEmailOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._to = None
        self._subject = None
        self._cc = None
        self._bcc = None
        self.discriminator = None

        self.to = to
        if subject is not None:
            self.subject = subject
        if cc is not None:
            self.cc = cc
        if bcc is not None:
            self.bcc = bcc

    @property
    def to(self):
        """Gets the to of this ForwardEmailOptions.  # noqa: E501


        :return: The to of this ForwardEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ForwardEmailOptions.


        :param to: The to of this ForwardEmailOptions.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def subject(self):
        """Gets the subject of this ForwardEmailOptions.  # noqa: E501


        :return: The subject of this ForwardEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ForwardEmailOptions.


        :param subject: The subject of this ForwardEmailOptions.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def cc(self):
        """Gets the cc of this ForwardEmailOptions.  # noqa: E501


        :return: The cc of this ForwardEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this ForwardEmailOptions.


        :param cc: The cc of this ForwardEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._cc = cc

    @property
    def bcc(self):
        """Gets the bcc of this ForwardEmailOptions.  # noqa: E501


        :return: The bcc of this ForwardEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this ForwardEmailOptions.


        :param bcc: The bcc of this ForwardEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._bcc = bcc

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
        if not isinstance(other, ForwardEmailOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ForwardEmailOptions):
            return True

        return self.to_dict() != other.to_dict()
