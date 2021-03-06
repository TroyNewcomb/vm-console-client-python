# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rapid7vmconsole.models.report_config_database_credentials_resource import ReportConfigDatabaseCredentialsResource  # noqa: F401,E501


class ReportConfigDatabaseResource(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'credentials': 'ReportConfigDatabaseCredentialsResource',
        'host': 'str',
        'name': 'str',
        'port': 'int',
        'vendor': 'str'
    }

    attribute_map = {
        'credentials': 'credentials',
        'host': 'host',
        'name': 'name',
        'port': 'port',
        'vendor': 'vendor'
    }

    def __init__(self, credentials=None, host=None, name=None, port=None, vendor=None):  # noqa: E501
        """ReportConfigDatabaseResource - a model defined in Swagger"""  # noqa: E501

        self._credentials = None
        self._host = None
        self._name = None
        self._port = None
        self._vendor = None
        self.discriminator = None

        if credentials is not None:
            self.credentials = credentials
        if host is not None:
            self.host = host
        if name is not None:
            self.name = name
        if port is not None:
            self.port = port
        if vendor is not None:
            self.vendor = vendor

    @property
    def credentials(self):
        """Gets the credentials of this ReportConfigDatabaseResource.  # noqa: E501

        ${report.config.database.credentials.description}  # noqa: E501

        :return: The credentials of this ReportConfigDatabaseResource.  # noqa: E501
        :rtype: ReportConfigDatabaseCredentialsResource
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this ReportConfigDatabaseResource.

        ${report.config.database.credentials.description}  # noqa: E501

        :param credentials: The credentials of this ReportConfigDatabaseResource.  # noqa: E501
        :type: ReportConfigDatabaseCredentialsResource
        """

        self._credentials = credentials

    @property
    def host(self):
        """Gets the host of this ReportConfigDatabaseResource.  # noqa: E501

        The database server host to export to.  # noqa: E501

        :return: The host of this ReportConfigDatabaseResource.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ReportConfigDatabaseResource.

        The database server host to export to.  # noqa: E501

        :param host: The host of this ReportConfigDatabaseResource.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def name(self):
        """Gets the name of this ReportConfigDatabaseResource.  # noqa: E501

        The name of the database to export to.  # noqa: E501

        :return: The name of this ReportConfigDatabaseResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportConfigDatabaseResource.

        The name of the database to export to.  # noqa: E501

        :param name: The name of this ReportConfigDatabaseResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def port(self):
        """Gets the port of this ReportConfigDatabaseResource.  # noqa: E501

        The database server port to export to.  # noqa: E501

        :return: The port of this ReportConfigDatabaseResource.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ReportConfigDatabaseResource.

        The database server port to export to.  # noqa: E501

        :param port: The port of this ReportConfigDatabaseResource.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def vendor(self):
        """Gets the vendor of this ReportConfigDatabaseResource.  # noqa: E501

        The type of the database server.  # noqa: E501

        :return: The vendor of this ReportConfigDatabaseResource.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this ReportConfigDatabaseResource.

        The type of the database server.  # noqa: E501

        :param vendor: The vendor of this ReportConfigDatabaseResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["oracle", "mssql", "mysql"]  # noqa: E501
        if vendor not in allowed_values:
            raise ValueError(
                "Invalid value for `vendor` ({0}), must be one of {1}"  # noqa: E501
                .format(vendor, allowed_values)
            )

        self._vendor = vendor

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ReportConfigDatabaseResource, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReportConfigDatabaseResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
