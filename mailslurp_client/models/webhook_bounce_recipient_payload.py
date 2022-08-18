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


class WebhookBounceRecipientPayload(object):
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
        'message_id': 'str',
        'webhook_id': 'str',
        'event_name': 'str',
        'webhook_name': 'str',
        'recipient': 'str'
    }

    attribute_map = {
        'message_id': 'messageId',
        'webhook_id': 'webhookId',
        'event_name': 'eventName',
        'webhook_name': 'webhookName',
        'recipient': 'recipient'
    }

    def __init__(self, message_id=None, webhook_id=None, event_name=None, webhook_name=None, recipient=None, local_vars_configuration=None):  # noqa: E501
        """WebhookBounceRecipientPayload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message_id = None
        self._webhook_id = None
        self._event_name = None
        self._webhook_name = None
        self._recipient = None
        self.discriminator = None

        self.message_id = message_id
        self.webhook_id = webhook_id
        self.event_name = event_name
        if webhook_name is not None:
            self.webhook_name = webhook_name
        self.recipient = recipient

    @property
    def message_id(self):
        """Gets the message_id of this WebhookBounceRecipientPayload.  # noqa: E501

        Idempotent message ID. Store this ID locally or in a database to prevent message duplication.  # noqa: E501

        :return: The message_id of this WebhookBounceRecipientPayload.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this WebhookBounceRecipientPayload.

        Idempotent message ID. Store this ID locally or in a database to prevent message duplication.  # noqa: E501

        :param message_id: The message_id of this WebhookBounceRecipientPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message_id is None:  # noqa: E501
            raise ValueError("Invalid value for `message_id`, must not be `None`")  # noqa: E501

        self._message_id = message_id

    @property
    def webhook_id(self):
        """Gets the webhook_id of this WebhookBounceRecipientPayload.  # noqa: E501

        ID of webhook entity being triggered  # noqa: E501

        :return: The webhook_id of this WebhookBounceRecipientPayload.  # noqa: E501
        :rtype: str
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this WebhookBounceRecipientPayload.

        ID of webhook entity being triggered  # noqa: E501

        :param webhook_id: The webhook_id of this WebhookBounceRecipientPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and webhook_id is None:  # noqa: E501
            raise ValueError("Invalid value for `webhook_id`, must not be `None`")  # noqa: E501

        self._webhook_id = webhook_id

    @property
    def event_name(self):
        """Gets the event_name of this WebhookBounceRecipientPayload.  # noqa: E501

        Name of the event type webhook is being triggered for.  # noqa: E501

        :return: The event_name of this WebhookBounceRecipientPayload.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this WebhookBounceRecipientPayload.

        Name of the event type webhook is being triggered for.  # noqa: E501

        :param event_name: The event_name of this WebhookBounceRecipientPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and event_name is None:  # noqa: E501
            raise ValueError("Invalid value for `event_name`, must not be `None`")  # noqa: E501
        allowed_values = ["EMAIL_RECEIVED", "NEW_EMAIL", "NEW_CONTACT", "NEW_ATTACHMENT", "EMAIL_OPENED", "EMAIL_READ", "DELIVERY_STATUS", "BOUNCE", "BOUNCE_RECIPIENT", "NEW_SMS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and event_name not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `event_name` ({0}), must be one of {1}"  # noqa: E501
                .format(event_name, allowed_values)
            )

        self._event_name = event_name

    @property
    def webhook_name(self):
        """Gets the webhook_name of this WebhookBounceRecipientPayload.  # noqa: E501

        Name of the webhook being triggered  # noqa: E501

        :return: The webhook_name of this WebhookBounceRecipientPayload.  # noqa: E501
        :rtype: str
        """
        return self._webhook_name

    @webhook_name.setter
    def webhook_name(self, webhook_name):
        """Sets the webhook_name of this WebhookBounceRecipientPayload.

        Name of the webhook being triggered  # noqa: E501

        :param webhook_name: The webhook_name of this WebhookBounceRecipientPayload.  # noqa: E501
        :type: str
        """

        self._webhook_name = webhook_name

    @property
    def recipient(self):
        """Gets the recipient of this WebhookBounceRecipientPayload.  # noqa: E501

        Email address that caused a bounce. Make note of the address and try not to message it again to preserve your reputation.  # noqa: E501

        :return: The recipient of this WebhookBounceRecipientPayload.  # noqa: E501
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this WebhookBounceRecipientPayload.

        Email address that caused a bounce. Make note of the address and try not to message it again to preserve your reputation.  # noqa: E501

        :param recipient: The recipient of this WebhookBounceRecipientPayload.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and recipient is None:  # noqa: E501
            raise ValueError("Invalid value for `recipient`, must not be `None`")  # noqa: E501

        self._recipient = recipient

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
        if not isinstance(other, WebhookBounceRecipientPayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookBounceRecipientPayload):
            return True

        return self.to_dict() != other.to_dict()
