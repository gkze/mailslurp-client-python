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


class ReplyToEmailOptions(object):
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
        'body': 'str',
        '_from': 'str',
        'reply_to': 'str',
        'charset': 'str',
        'attachments': 'list[str]',
        'template_variables': 'dict(str, object)',
        'template': 'str',
        'send_strategy': 'str',
        'use_inbox_name': 'bool',
        'html': 'bool'
    }

    attribute_map = {
        'body': 'body',
        '_from': 'from',
        'reply_to': 'replyTo',
        'charset': 'charset',
        'attachments': 'attachments',
        'template_variables': 'templateVariables',
        'template': 'template',
        'send_strategy': 'sendStrategy',
        'use_inbox_name': 'useInboxName',
        'html': 'html'
    }

    def __init__(self, body=None, _from=None, reply_to=None, charset=None, attachments=None, template_variables=None, template=None, send_strategy=None, use_inbox_name=None, html=None, local_vars_configuration=None):  # noqa: E501
        """ReplyToEmailOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._body = None
        self.__from = None
        self._reply_to = None
        self._charset = None
        self._attachments = None
        self._template_variables = None
        self._template = None
        self._send_strategy = None
        self._use_inbox_name = None
        self._html = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if _from is not None:
            self._from = _from
        if reply_to is not None:
            self.reply_to = reply_to
        if charset is not None:
            self.charset = charset
        if attachments is not None:
            self.attachments = attachments
        if template_variables is not None:
            self.template_variables = template_variables
        if template is not None:
            self.template = template
        if send_strategy is not None:
            self.send_strategy = send_strategy
        if use_inbox_name is not None:
            self.use_inbox_name = use_inbox_name
        if html is not None:
            self.html = html

    @property
    def body(self):
        """Gets the body of this ReplyToEmailOptions.  # noqa: E501

        Body of the reply email you want to send  # noqa: E501

        :return: The body of this ReplyToEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ReplyToEmailOptions.

        Body of the reply email you want to send  # noqa: E501

        :param body: The body of this ReplyToEmailOptions.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def _from(self):
        """Gets the _from of this ReplyToEmailOptions.  # noqa: E501

        The from header that should be used. Optional  # noqa: E501

        :return: The _from of this ReplyToEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ReplyToEmailOptions.

        The from header that should be used. Optional  # noqa: E501

        :param _from: The _from of this ReplyToEmailOptions.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def reply_to(self):
        """Gets the reply_to of this ReplyToEmailOptions.  # noqa: E501

        The replyTo header that should be used. Optional  # noqa: E501

        :return: The reply_to of this ReplyToEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this ReplyToEmailOptions.

        The replyTo header that should be used. Optional  # noqa: E501

        :param reply_to: The reply_to of this ReplyToEmailOptions.  # noqa: E501
        :type: str
        """

        self._reply_to = reply_to

    @property
    def charset(self):
        """Gets the charset of this ReplyToEmailOptions.  # noqa: E501

        The charset that your message should be sent with. Optional. Default is UTF-8  # noqa: E501

        :return: The charset of this ReplyToEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._charset

    @charset.setter
    def charset(self, charset):
        """Sets the charset of this ReplyToEmailOptions.

        The charset that your message should be sent with. Optional. Default is UTF-8  # noqa: E501

        :param charset: The charset of this ReplyToEmailOptions.  # noqa: E501
        :type: str
        """

        self._charset = charset

    @property
    def attachments(self):
        """Gets the attachments of this ReplyToEmailOptions.  # noqa: E501

        List of uploaded attachments to send with the reply. Optional.  # noqa: E501

        :return: The attachments of this ReplyToEmailOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this ReplyToEmailOptions.

        List of uploaded attachments to send with the reply. Optional.  # noqa: E501

        :param attachments: The attachments of this ReplyToEmailOptions.  # noqa: E501
        :type: list[str]
        """

        self._attachments = attachments

    @property
    def template_variables(self):
        """Gets the template_variables of this ReplyToEmailOptions.  # noqa: E501

        Template variables if using a template  # noqa: E501

        :return: The template_variables of this ReplyToEmailOptions.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._template_variables

    @template_variables.setter
    def template_variables(self, template_variables):
        """Sets the template_variables of this ReplyToEmailOptions.

        Template variables if using a template  # noqa: E501

        :param template_variables: The template_variables of this ReplyToEmailOptions.  # noqa: E501
        :type: dict(str, object)
        """

        self._template_variables = template_variables

    @property
    def template(self):
        """Gets the template of this ReplyToEmailOptions.  # noqa: E501

        Template ID to use instead of body. Will use template variable map to fill defined variable slots.  # noqa: E501

        :return: The template of this ReplyToEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ReplyToEmailOptions.

        Template ID to use instead of body. Will use template variable map to fill defined variable slots.  # noqa: E501

        :param template: The template of this ReplyToEmailOptions.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def send_strategy(self):
        """Gets the send_strategy of this ReplyToEmailOptions.  # noqa: E501

        How an email should be sent based on its recipients  # noqa: E501

        :return: The send_strategy of this ReplyToEmailOptions.  # noqa: E501
        :rtype: str
        """
        return self._send_strategy

    @send_strategy.setter
    def send_strategy(self, send_strategy):
        """Sets the send_strategy of this ReplyToEmailOptions.

        How an email should be sent based on its recipients  # noqa: E501

        :param send_strategy: The send_strategy of this ReplyToEmailOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["SINGLE_MESSAGE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and send_strategy not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `send_strategy` ({0}), must be one of {1}"  # noqa: E501
                .format(send_strategy, allowed_values)
            )

        self._send_strategy = send_strategy

    @property
    def use_inbox_name(self):
        """Gets the use_inbox_name of this ReplyToEmailOptions.  # noqa: E501

        Optionally use inbox name as display name for sender email address  # noqa: E501

        :return: The use_inbox_name of this ReplyToEmailOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_inbox_name

    @use_inbox_name.setter
    def use_inbox_name(self, use_inbox_name):
        """Sets the use_inbox_name of this ReplyToEmailOptions.

        Optionally use inbox name as display name for sender email address  # noqa: E501

        :param use_inbox_name: The use_inbox_name of this ReplyToEmailOptions.  # noqa: E501
        :type: bool
        """

        self._use_inbox_name = use_inbox_name

    @property
    def html(self):
        """Gets the html of this ReplyToEmailOptions.  # noqa: E501


        :return: The html of this ReplyToEmailOptions.  # noqa: E501
        :rtype: bool
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this ReplyToEmailOptions.


        :param html: The html of this ReplyToEmailOptions.  # noqa: E501
        :type: bool
        """

        self._html = html

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
        if not isinstance(other, ReplyToEmailOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReplyToEmailOptions):
            return True

        return self.to_dict() != other.to_dict()
