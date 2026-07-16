

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PayslipSummary(UniversalBaseModel):
    deductions: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Deductions")] = pydantic.Field(
        default=None
    )
    """
    The Deductions for the Payslip
    """

    employee_group: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="EmployeeGroup")] = (
        pydantic.Field(default=None)
    )
    """
    Employee group name
    """

    employee_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="EmployeeID")] = pydantic.Field(
        default=None
    )
    """
    The Xero identifier for an employee
    """

    first_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="FirstName")] = pydantic.Field(
        default=None
    )
    """
    First name of employee
    """

    last_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="LastName")] = pydantic.Field(
        default=None
    )
    """
    Last name of employee
    """

    net_pay: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="NetPay")] = pydantic.Field(
        default=None
    )
    """
    The NetPay for the Payslip
    """

    payslip_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="PayslipID")] = pydantic.Field(
        default=None
    )
    """
    Xero identifier for the payslip
    """

    reimbursements: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Reimbursements")] = (
        pydantic.Field(default=None)
    )
    """
    The Reimbursements for the Payslip
    """

    super: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Super")] = pydantic.Field(
        default=None
    )
    """
    The Super for the Payslip
    """

    tax: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Tax")] = pydantic.Field(default=None)
    """
    The Tax for the Payslip
    """

    updated_date_utc: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="UpdatedDateUTC")] = (
        pydantic.Field(default=None)
    )
    """
    Last modified timestamp
    """

    wages: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Wages")] = pydantic.Field(
        default=None
    )
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
