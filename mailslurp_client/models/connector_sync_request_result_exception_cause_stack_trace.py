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


class ConnectorSyncRequestResultExceptionCauseStackTrace(object):
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
        'class_loader_name': 'str',
        'module_name': 'str',
        'module_version': 'str',
        'method_name': 'str',
        'file_name': 'str',
        'line_number': 'int',
        'native_method': 'bool',
        'class_name': 'str'
    }

    attribute_map = {
        'class_loader_name': 'classLoaderName',
        'module_name': 'moduleName',
        'module_version': 'moduleVersion',
        'method_name': 'methodName',
        'file_name': 'fileName',
        'line_number': 'lineNumber',
        'native_method': 'nativeMethod',
        'class_name': 'className'
    }

    def __init__(self, class_loader_name=None, module_name=None, module_version=None, method_name=None, file_name=None, line_number=None, native_method=None, class_name=None, local_vars_configuration=None):  # noqa: E501
        """ConnectorSyncRequestResultExceptionCauseStackTrace - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._class_loader_name = None
        self._module_name = None
        self._module_version = None
        self._method_name = None
        self._file_name = None
        self._line_number = None
        self._native_method = None
        self._class_name = None
        self.discriminator = None

        if class_loader_name is not None:
            self.class_loader_name = class_loader_name
        if module_name is not None:
            self.module_name = module_name
        if module_version is not None:
            self.module_version = module_version
        if method_name is not None:
            self.method_name = method_name
        if file_name is not None:
            self.file_name = file_name
        if line_number is not None:
            self.line_number = line_number
        if native_method is not None:
            self.native_method = native_method
        if class_name is not None:
            self.class_name = class_name

    @property
    def class_loader_name(self):
        """Gets the class_loader_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501


        :return: The class_loader_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :rtype: str
        """
        return self._class_loader_name

    @class_loader_name.setter
    def class_loader_name(self, class_loader_name):
        """Sets the class_loader_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.


        :param class_loader_name: The class_loader_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :type: str
        """

        self._class_loader_name = class_loader_name

    @property
    def module_name(self):
        """Gets the module_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501


        :return: The module_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """Sets the module_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.


        :param module_name: The module_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :type: str
        """

        self._module_name = module_name

    @property
    def module_version(self):
        """Gets the module_version of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501


        :return: The module_version of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :rtype: str
        """
        return self._module_version

    @module_version.setter
    def module_version(self, module_version):
        """Sets the module_version of this ConnectorSyncRequestResultExceptionCauseStackTrace.


        :param module_version: The module_version of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :type: str
        """

        self._module_version = module_version

    @property
    def method_name(self):
        """Gets the method_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501


        :return: The method_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :rtype: str
        """
        return self._method_name

    @method_name.setter
    def method_name(self, method_name):
        """Sets the method_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.


        :param method_name: The method_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :type: str
        """

        self._method_name = method_name

    @property
    def file_name(self):
        """Gets the file_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501


        :return: The file_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.


        :param file_name: The file_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def line_number(self):
        """Gets the line_number of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501


        :return: The line_number of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """Sets the line_number of this ConnectorSyncRequestResultExceptionCauseStackTrace.


        :param line_number: The line_number of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :type: int
        """

        self._line_number = line_number

    @property
    def native_method(self):
        """Gets the native_method of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501


        :return: The native_method of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :rtype: bool
        """
        return self._native_method

    @native_method.setter
    def native_method(self, native_method):
        """Sets the native_method of this ConnectorSyncRequestResultExceptionCauseStackTrace.


        :param native_method: The native_method of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :type: bool
        """

        self._native_method = native_method

    @property
    def class_name(self):
        """Gets the class_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501


        :return: The class_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.


        :param class_name: The class_name of this ConnectorSyncRequestResultExceptionCauseStackTrace.  # noqa: E501
        :type: str
        """

        self._class_name = class_name

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
        if not isinstance(other, ConnectorSyncRequestResultExceptionCauseStackTrace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectorSyncRequestResultExceptionCauseStackTrace):
            return True

        return self.to_dict() != other.to_dict()
