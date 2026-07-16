

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bank_account import BankAccount
from .employee_gender import EmployeeGender
from .employee_status import EmployeeStatus
from .home_address import HomeAddress
from .leave_balance import LeaveBalance
from .leave_line import LeaveLine
from .opening_balances import OpeningBalances
from .pay_template import PayTemplate
from .super_membership import SuperMembership
from .tax_declaration import TaxDeclaration
from .validation_error import ValidationError


class Employee(UniversalBaseModel):
    bank_accounts: typing_extensions.Annotated[
        typing.Optional[typing.List[BankAccount]],
        FieldMetadata(alias="BankAccounts"),
        pydantic.Field(alias="BankAccounts"),
    ] = None
    classification: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Classification"),
        pydantic.Field(alias="Classification", description="Employees classification"),
    ] = None
    """
    Employees classification
    """

    date_of_birth: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="DateOfBirth"),
        pydantic.Field(alias="DateOfBirth", description="Date of birth of the employee (YYYY-MM-DD)"),
    ]
    """
    Date of birth of the employee (YYYY-MM-DD)
    """

    email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Email"),
        pydantic.Field(alias="Email", description="The email address for the employee"),
    ] = None
    """
    The email address for the employee
    """

    employee_group_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="EmployeeGroupName"),
        pydantic.Field(
            alias="EmployeeGroupName",
            description="The Employee Group allows you to report on payroll expenses and liabilities for each group of employees",
        ),
    ] = None
    """
    The Employee Group allows you to report on payroll expenses and liabilities for each group of employees
    """

    employee_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="EmployeeID"),
        pydantic.Field(alias="EmployeeID", description="Xero unique identifier for an Employee"),
    ] = None
    """
    Xero unique identifier for an Employee
    """

    first_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="FirstName"), pydantic.Field(alias="FirstName", description="First name of employee")
    ]
    """
    First name of employee
    """

    gender: typing_extensions.Annotated[
        typing.Optional[EmployeeGender],
        FieldMetadata(alias="Gender"),
        pydantic.Field(alias="Gender", description="The employee’s gender. See Employee Gender"),
    ] = None
    """
    The employee’s gender. See Employee Gender
    """

    home_address: typing_extensions.Annotated[
        typing.Optional[HomeAddress], FieldMetadata(alias="HomeAddress"), pydantic.Field(alias="HomeAddress")
    ] = None
    is_authorised_to_approve_leave: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="IsAuthorisedToApproveLeave"),
        pydantic.Field(
            alias="IsAuthorisedToApproveLeave", description="Authorised to approve other employees' leave requests"
        ),
    ] = None
    """
    Authorised to approve other employees' leave requests
    """

    is_authorised_to_approve_timesheets: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="IsAuthorisedToApproveTimesheets"),
        pydantic.Field(alias="IsAuthorisedToApproveTimesheets", description="Authorised to approve timesheets"),
    ] = None
    """
    Authorised to approve timesheets
    """

    job_title: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="JobTitle"),
        pydantic.Field(alias="JobTitle", description="JobTitle of the employee"),
    ] = None
    """
    JobTitle of the employee
    """

    last_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="LastName"), pydantic.Field(alias="LastName", description="Last name of employee")
    ]
    """
    Last name of employee
    """

    leave_balances: typing_extensions.Annotated[
        typing.Optional[typing.List[LeaveBalance]],
        FieldMetadata(alias="LeaveBalances"),
        pydantic.Field(alias="LeaveBalances"),
    ] = None
    leave_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[LeaveLine]], FieldMetadata(alias="LeaveLines"), pydantic.Field(alias="LeaveLines")
    ] = None
    middle_names: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="MiddleNames"),
        pydantic.Field(alias="MiddleNames", description="Middle name(s) of the employee"),
    ] = None
    """
    Middle name(s) of the employee
    """

    mobile: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Mobile"),
        pydantic.Field(alias="Mobile", description="Employee mobile number"),
    ] = None
    """
    Employee mobile number
    """

    opening_balances: typing_extensions.Annotated[
        typing.Optional[OpeningBalances],
        FieldMetadata(alias="OpeningBalances"),
        pydantic.Field(alias="OpeningBalances"),
    ] = None
    ordinary_earnings_rate_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OrdinaryEarningsRateID"),
        pydantic.Field(alias="OrdinaryEarningsRateID", description="Xero unique identifier for earnings rate"),
    ] = None
    """
    Xero unique identifier for earnings rate
    """

    pay_template: typing_extensions.Annotated[
        typing.Optional[PayTemplate], FieldMetadata(alias="PayTemplate"), pydantic.Field(alias="PayTemplate")
    ] = None
    payroll_calendar_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PayrollCalendarID"),
        pydantic.Field(
            alias="PayrollCalendarID", description="Xero unique identifier for payroll calendar for the employee"
        ),
    ] = None
    """
    Xero unique identifier for payroll calendar for the employee
    """

    phone: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Phone"),
        pydantic.Field(alias="Phone", description="Employee phone number"),
    ] = None
    """
    Employee phone number
    """

    start_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StartDate"),
        pydantic.Field(alias="StartDate", description="Start date for an employee (YYYY-MM-DD)"),
    ] = None
    """
    Start date for an employee (YYYY-MM-DD)
    """

    status: typing_extensions.Annotated[
        typing.Optional[EmployeeStatus], FieldMetadata(alias="Status"), pydantic.Field(alias="Status")
    ] = None
    super_memberships: typing_extensions.Annotated[
        typing.Optional[typing.List[SuperMembership]],
        FieldMetadata(alias="SuperMemberships"),
        pydantic.Field(alias="SuperMemberships"),
    ] = None
    tax_declaration: typing_extensions.Annotated[
        typing.Optional[TaxDeclaration], FieldMetadata(alias="TaxDeclaration"), pydantic.Field(alias="TaxDeclaration")
    ] = None
    termination_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TerminationDate"),
        pydantic.Field(alias="TerminationDate", description="Employee Termination Date (YYYY-MM-DD)"),
    ] = None
    """
    Employee Termination Date (YYYY-MM-DD)
    """

    title: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Title"),
        pydantic.Field(alias="Title", description="Title of the employee"),
    ] = None
    """
    Title of the employee
    """

    twitter_user_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TwitterUserName"),
        pydantic.Field(alias="TwitterUserName", description="Employee’s twitter name"),
    ] = None
    """
    Employee’s twitter name
    """

    updated_date_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="UpdatedDateUTC"),
        pydantic.Field(alias="UpdatedDateUTC", description="Last modified timestamp"),
    ] = None
    """
    Last modified timestamp
    """

    validation_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[ValidationError]],
        FieldMetadata(alias="ValidationErrors"),
        pydantic.Field(
            alias="ValidationErrors", description="Displays array of validation error messages from the API"
        ),
    ] = None
    """
    Displays array of validation error messages from the API
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
