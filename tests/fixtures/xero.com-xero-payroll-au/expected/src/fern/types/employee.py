

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
        typing.Optional[typing.List[BankAccount]], FieldMetadata(alias="BankAccounts")
    ] = None
    classification: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Classification")] = (
        pydantic.Field(default=None)
    )
    """
    Employees classification
    """

    date_of_birth: typing_extensions.Annotated[str, FieldMetadata(alias="DateOfBirth")] = pydantic.Field()
    """
    Date of birth of the employee (YYYY-MM-DD)
    """

    email: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Email")] = pydantic.Field(
        default=None
    )
    """
    The email address for the employee
    """

    employee_group_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="EmployeeGroupName")] = (
        pydantic.Field(default=None)
    )
    """
    The Employee Group allows you to report on payroll expenses and liabilities for each group of employees
    """

    employee_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="EmployeeID")] = pydantic.Field(
        default=None
    )
    """
    Xero unique identifier for an Employee
    """

    first_name: typing_extensions.Annotated[str, FieldMetadata(alias="FirstName")] = pydantic.Field()
    """
    First name of employee
    """

    gender: typing_extensions.Annotated[typing.Optional[EmployeeGender], FieldMetadata(alias="Gender")] = (
        pydantic.Field(default=None)
    )
    """
    The employee’s gender. See Employee Gender
    """

    home_address: typing_extensions.Annotated[typing.Optional[HomeAddress], FieldMetadata(alias="HomeAddress")] = None
    is_authorised_to_approve_leave: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="IsAuthorisedToApproveLeave")
    ] = pydantic.Field(default=None)
    """
    Authorised to approve other employees' leave requests
    """

    is_authorised_to_approve_timesheets: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="IsAuthorisedToApproveTimesheets")
    ] = pydantic.Field(default=None)
    """
    Authorised to approve timesheets
    """

    job_title: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="JobTitle")] = pydantic.Field(
        default=None
    )
    """
    JobTitle of the employee
    """

    last_name: typing_extensions.Annotated[str, FieldMetadata(alias="LastName")] = pydantic.Field()
    """
    Last name of employee
    """

    leave_balances: typing_extensions.Annotated[
        typing.Optional[typing.List[LeaveBalance]], FieldMetadata(alias="LeaveBalances")
    ] = None
    leave_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[LeaveLine]], FieldMetadata(alias="LeaveLines")
    ] = None
    middle_names: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="MiddleNames")] = (
        pydantic.Field(default=None)
    )
    """
    Middle name(s) of the employee
    """

    mobile: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Mobile")] = pydantic.Field(
        default=None
    )
    """
    Employee mobile number
    """

    opening_balances: typing_extensions.Annotated[
        typing.Optional[OpeningBalances], FieldMetadata(alias="OpeningBalances")
    ] = None
    ordinary_earnings_rate_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="OrdinaryEarningsRateID")
    ] = pydantic.Field(default=None)
    """
    Xero unique identifier for earnings rate
    """

    pay_template: typing_extensions.Annotated[typing.Optional[PayTemplate], FieldMetadata(alias="PayTemplate")] = None
    payroll_calendar_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="PayrollCalendarID")] = (
        pydantic.Field(default=None)
    )
    """
    Xero unique identifier for payroll calendar for the employee
    """

    phone: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Phone")] = pydantic.Field(
        default=None
    )
    """
    Employee phone number
    """

    start_date: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="StartDate")] = pydantic.Field(
        default=None
    )
    """
    Start date for an employee (YYYY-MM-DD)
    """

    status: typing_extensions.Annotated[typing.Optional[EmployeeStatus], FieldMetadata(alias="Status")] = None
    super_memberships: typing_extensions.Annotated[
        typing.Optional[typing.List[SuperMembership]], FieldMetadata(alias="SuperMemberships")
    ] = None
    tax_declaration: typing_extensions.Annotated[
        typing.Optional[TaxDeclaration], FieldMetadata(alias="TaxDeclaration")
    ] = None
    termination_date: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TerminationDate")] = (
        pydantic.Field(default=None)
    )
    """
    Employee Termination Date (YYYY-MM-DD)
    """

    title: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Title")] = pydantic.Field(
        default=None
    )
    """
    Title of the employee
    """

    twitter_user_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TwitterUserName")] = (
        pydantic.Field(default=None)
    )
    """
    Employee’s twitter name
    """

    updated_date_utc: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="UpdatedDateUTC")] = (
        pydantic.Field(default=None)
    )
    """
    Last modified timestamp
    """

    validation_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[ValidationError]], FieldMetadata(alias="ValidationErrors")
    ] = pydantic.Field(default=None)
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
