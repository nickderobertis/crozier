

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .deduction_line import DeductionLine
from .earnings_line import EarningsLine
from .leave_accrual_line import LeaveAccrualLine
from .leave_earnings_line import LeaveEarningsLine
from .reimbursement_line import ReimbursementLine
from .superannuation_line import SuperannuationLine
from .tax_line import TaxLine


class Payslip(UniversalBaseModel):
    deduction_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[DeductionLine]],
        FieldMetadata(alias="DeductionLines"),
        pydantic.Field(alias="DeductionLines"),
    ] = None
    deductions: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Deductions"),
        pydantic.Field(alias="Deductions", description="The Deductions for the Payslip"),
    ] = None
    """
    The Deductions for the Payslip
    """

    earnings_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[EarningsLine]],
        FieldMetadata(alias="EarningsLines"),
        pydantic.Field(alias="EarningsLines"),
    ] = None
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

    leave_accrual_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[LeaveAccrualLine]],
        FieldMetadata(alias="LeaveAccrualLines"),
        pydantic.Field(alias="LeaveAccrualLines"),
    ] = None
    leave_earnings_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[LeaveEarningsLine]],
        FieldMetadata(alias="LeaveEarningsLines"),
        pydantic.Field(alias="LeaveEarningsLines"),
    ] = None
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

    reimbursement_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[ReimbursementLine]],
        FieldMetadata(alias="ReimbursementLines"),
        pydantic.Field(alias="ReimbursementLines"),
    ] = None
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

    superannuation_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[SuperannuationLine]],
        FieldMetadata(alias="SuperannuationLines"),
        pydantic.Field(alias="SuperannuationLines"),
    ] = None
    tax: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="Tax"),
        pydantic.Field(alias="Tax", description="The Tax for the Payslip"),
    ] = None
    """
    The Tax for the Payslip
    """

    tax_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[TaxLine]], FieldMetadata(alias="TaxLines"), pydantic.Field(alias="TaxLines")
    ] = None
    timesheet_earnings_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[EarningsLine]],
        FieldMetadata(alias="TimesheetEarningsLines"),
        pydantic.Field(alias="TimesheetEarningsLines"),
    ] = None
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
