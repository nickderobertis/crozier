

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PayslipSummary(UniversalBaseModel):
    deductions: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Deductions"),
        pydantic.Field(alias="Deductions", description="The Deductions for the Payslip"),
    ] = None
    """
    The Deductions for the Payslip
    """

    employee_group: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="EmployeeGroup"),
        pydantic.Field(alias="EmployeeGroup", description="Employee group name"),
    ] = None
    """
    Employee group name
    """

    employee_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="EmployeeID"),
        pydantic.Field(alias="EmployeeID", description="The Xero identifier for an employee"),
    ] = None
    """
    The Xero identifier for an employee
    """

    first_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FirstName"),
        pydantic.Field(alias="FirstName", description="First name of employee"),
    ] = None
    """
    First name of employee
    """

    last_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LastName"),
        pydantic.Field(alias="LastName", description="Last name of employee"),
    ] = None
    """
    Last name of employee
    """

    net_pay: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="NetPay"),
        pydantic.Field(alias="NetPay", description="The NetPay for the Payslip"),
    ] = None
    """
    The NetPay for the Payslip
    """

    payslip_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PayslipID"),
        pydantic.Field(alias="PayslipID", description="Xero identifier for the payslip"),
    ] = None
    """
    Xero identifier for the payslip
    """

    reimbursements: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Reimbursements"),
        pydantic.Field(alias="Reimbursements", description="The Reimbursements for the Payslip"),
    ] = None
    """
    The Reimbursements for the Payslip
    """

    super: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Super"),
        pydantic.Field(alias="Super", description="The Super for the Payslip"),
    ] = None
    """
    The Super for the Payslip
    """

    tax: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Tax"),
        pydantic.Field(alias="Tax", description="The Tax for the Payslip"),
    ] = None
    """
    The Tax for the Payslip
    """

    updated_date_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="UpdatedDateUTC"),
        pydantic.Field(alias="UpdatedDateUTC", description="Last modified timestamp"),
    ] = None
    """
    Last modified timestamp
    """

    wages: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Wages"),
        pydantic.Field(alias="Wages", description="The Wages for the Payslip"),
    ] = None
    """
    The Wages for the Payslip
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
