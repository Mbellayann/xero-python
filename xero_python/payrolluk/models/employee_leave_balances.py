# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.2.10
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EmployeeLeaveBalances(BaseModel):
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
        "pagination": "Pagination",
        "problem": "Problem",
        "leave_balances": "list[EmployeeLeaveBalance]",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "leave_balances": "leaveBalances",
    }

    def __init__(
        self, pagination=None, problem=None, leave_balances=None
    ):  # noqa: E501
        """EmployeeLeaveBalances - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._leave_balances = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if leave_balances is not None:
            self.leave_balances = leave_balances

    @property
    def pagination(self):
        """Gets the pagination of this EmployeeLeaveBalances.  # noqa: E501


        :return: The pagination of this EmployeeLeaveBalances.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this EmployeeLeaveBalances.


        :param pagination: The pagination of this EmployeeLeaveBalances.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this EmployeeLeaveBalances.  # noqa: E501


        :return: The problem of this EmployeeLeaveBalances.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this EmployeeLeaveBalances.


        :param problem: The problem of this EmployeeLeaveBalances.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def leave_balances(self):
        """Gets the leave_balances of this EmployeeLeaveBalances.  # noqa: E501


        :return: The leave_balances of this EmployeeLeaveBalances.  # noqa: E501
        :rtype: list[EmployeeLeaveBalance]
        """
        return self._leave_balances

    @leave_balances.setter
    def leave_balances(self, leave_balances):
        """Sets the leave_balances of this EmployeeLeaveBalances.


        :param leave_balances: The leave_balances of this EmployeeLeaveBalances.  # noqa: E501
        :type: list[EmployeeLeaveBalance]
        """

        self._leave_balances = leave_balances