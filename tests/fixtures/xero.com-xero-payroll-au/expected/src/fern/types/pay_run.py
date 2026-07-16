

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pay_run_status import PayRunStatus
from .payslip_summary import PayslipSummary
from .validation_error import ValidationError


class PayRun(UniversalBaseModel):
    deductions: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Deductions")] = pydantic.Field(
        default=None
    )
    """
    The total Deductions for the Payrun
    """

    net_pay: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="NetPay")] = pydantic.Field(
        default=None
    )
    """
    The total NetPay for the Payrun
    """

    pay_run_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="PayRunID")] = pydantic.Field(
        default=None
    )
    """
    Xero identifier for pay run
    """

    pay_run_period_end_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PayRunPeriodEndDate")
    ] = pydantic.Field(default=None)
    """
    Period End Date for the PayRun (YYYY-MM-DD)
    """

    pay_run_period_start_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PayRunPeriodStartDate")
    ] = pydantic.Field(default=None)
    """
    Period Start Date for the PayRun (YYYY-MM-DD)
    """

    pay_run_status: typing_extensions.Annotated[typing.Optional[PayRunStatus], FieldMetadata(alias="PayRunStatus")] = (
        None
    )
    payment_date: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="PaymentDate")] = (
        pydantic.Field(default=None)
    )
    """
    Payment Date for the PayRun (YYYY-MM-DD)
    """

    payroll_calendar_id: typing_extensions.Annotated[str, FieldMetadata(alias="PayrollCalendarID")] = pydantic.Field()
    """
    Xero identifier for pay run
    """

    payslip_message: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="PayslipMessage")] = (
        pydantic.Field(default=None)
    )
    """
    Payslip message for the PayRun
    """

    payslips: typing_extensions.Annotated[
        typing.Optional[typing.List[PayslipSummary]], FieldMetadata(alias="Payslips")
    ] = pydantic.Field(default=None)
    """
    The payslips in the payrun
    """

    reimbursement: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Reimbursement")] = (
        pydantic.Field(default=None)
    )
    """
    The total Reimbursements for the Payrun
    """

    super: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Super")] = pydantic.Field(
        default=None
    )
    """
    The total Super for the Payrun
    """

    tax: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Tax")] = pydantic.Field(default=None)
    """
    The total Tax for the Payrun
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

    wages: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Wages")] = pydantic.Field(
        default=None
    )
    """
    The total Wages for the Payrun
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
