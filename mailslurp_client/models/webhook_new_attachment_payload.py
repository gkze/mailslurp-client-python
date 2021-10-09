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


class WebhookNewAttachmentPayload(object):
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
        'event_name': 'str',
        'message_id': 'str',
        'name': 'str',
        'webhook_id': 'str',
        'webhook_name': 'str'
    }

    attribute_map = {
        'attachment_id': 'attachmentId',
        'content_length': 'contentLength',
        'content_type': 'contentType',
        'event_name': 'eventName',
        'message_id': 'messageId',
        'name': 'name',
        'webhook_id': 'webhookId',
        'webhook_name': 'webhookName'
    }

    def __init__(self, attachment_id=None, content_length=None, content_type=None, event_name=None, message_id=None, name=None, webhook_id=None, webhook_name=None, local_vars_configuration=None):  # noqa: E501
        """WebhookNewAttachmentPayload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attachment_id = None
        self._content_length = None
        self._content_type = None
        self._event_name = None
        self._message_id = None
        self._name = None
        self._webhook_id = None
        self._webhook_name = None
        self.discriminator = None

        if attachment_id is not None:
            self.attachment_id = attachment_id
        if content_length is not None:
            self.content_length = content_length
        if content_type is not None:
            self.content_type = content_type
        if event_name is not None:
            self.event_name = event_name
        if message_id is not None:
            self.message_id = message_id
        if name is not None:
            self.name = name
        if webhook_id is not None:
            self.webhook_id = webhook_id
        if webhook_name is not None:
            self.webhook_name = webhook_name

    @property
    def attachment_id(self):
        """Gets the attachment_id of this WebhookNewAttachmentPayload.  # noqa: E501

        ID of attachment. Use the `AttachmentController` to  # noqa: E501

        :return: The attachment_id of this WebhookNewAttachmentPayload.  # noqa: E501
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this WebhookNewAttachmentPayload.

        ID of attachment. Use the `AttachmentController` to  # noqa: E501

        :param attachment_id: The attachment_id of this WebhookNewAttachmentPayload.  # noqa: E501
        :type: str
        """

        self._attachment_id = attachment_id

    @property
    def content_length(self):
        """Gets the content_length of this WebhookNewAttachmentPayload.  # noqa: E501

        Size of attachment in bytes  # noqa: E501

        :return: The content_length of this WebhookNewAttachmentPayload.  # noqa: E501
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this WebhookNewAttachmentPayload.

        Size of attachment in bytes  # noqa: E501

        :param content_length: The content_length of this WebhookNewAttachmentPayload.  # noqa: E501
        :type: int
        """

        self._content_length = content_length

    @property
    def content_type(self):
        """Gets the content_type of this WebhookNewAttachmentPayload.  # noqa: E501

        Content type of attachment such as 'image/png' or 'application/pdf  # noqa: E501

        :return: The content_type of this WebhookNewAttachmentPayload.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this WebhookNewAttachmentPayload.

        Content type of attachment such as 'image/png' or 'application/pdf  # noqa: E501

        :param content_type: The content_type of this WebhookNewAttachmentPayload.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def event_name(self):
        """Gets the event_name of this WebhookNewAttachmentPayload.  # noqa: E501

        Name of the event type webhook is being triggered for.  # noqa: E501

        :return: The event_name of this WebhookNewAttachmentPayload.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this WebhookNewAttachmentPayload.

        Name of the event type webhook is being triggered for.  # noqa: E501

        :param event_name: The event_name of this WebhookNewAttachmentPayload.  # noqa: E501
        :type: str
        """
        allowed_values = ["EMAIL_RECEIVED", "NEW_EMAIL", "NEW_CONTACT", "NEW_ATTACHMENT", "EMAIL_OPENED", "EMAIL_READ"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and event_name not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `event_name` ({0}), must be one of {1}"  # noqa: E501
                .format(event_name, allowed_values)
            )

        self._event_name = event_name

    @property
    def message_id(self):
        """Gets the message_id of this WebhookNewAttachmentPayload.  # noqa: E501

        Idempotent message ID. Store this ID locally or in a database to prevent message duplication.  # noqa: E501

        :return: The message_id of this WebhookNewAttachmentPayload.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this WebhookNewAttachmentPayload.

        Idempotent message ID. Store this ID locally or in a database to prevent message duplication.  # noqa: E501

        :param message_id: The message_id of this WebhookNewAttachmentPayload.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def name(self):
        """Gets the name of this WebhookNewAttachmentPayload.  # noqa: E501

        Filename of the attachment if present  # noqa: E501

        :return: The name of this WebhookNewAttachmentPayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebhookNewAttachmentPayload.

        Filename of the attachment if present  # noqa: E501

        :param name: The name of this WebhookNewAttachmentPayload.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def webhook_id(self):
        """Gets the webhook_id of this WebhookNewAttachmentPayload.  # noqa: E501

        ID of webhook entity being triggered  # noqa: E501

        :return: The webhook_id of this WebhookNewAttachmentPayload.  # noqa: E501
        :rtype: str
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this WebhookNewAttachmentPayload.

        ID of webhook entity being triggered  # noqa: E501

        :param webhook_id: The webhook_id of this WebhookNewAttachmentPayload.  # noqa: E501
        :type: str
        """

        self._webhook_id = webhook_id

    @property
    def webhook_name(self):
        """Gets the webhook_name of this WebhookNewAttachmentPayload.  # noqa: E501

        Name of the webhook being triggered  # noqa: E501

        :return: The webhook_name of this WebhookNewAttachmentPayload.  # noqa: E501
        :rtype: str
        """
        return self._webhook_name

    @webhook_name.setter
    def webhook_name(self, webhook_name):
        """Sets the webhook_name of this WebhookNewAttachmentPayload.

        Name of the webhook being triggered  # noqa: E501

        :param webhook_name: The webhook_name of this WebhookNewAttachmentPayload.  # noqa: E501
        :type: str
        """

        self._webhook_name = webhook_name

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
        if not isinstance(other, WebhookNewAttachmentPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookNewAttachmentPayload):
            return True

        return self.to_dict() != other.to_dict()
