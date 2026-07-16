

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


class PayslipLines(UniversalBaseModel):
    deduction_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[DeductionLine]], FieldMetadata(alias="DeductionLines")
    ] = None
    earnings_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[EarningsLine]], FieldMetadata(alias="EarningsLines")
    ] = None
    leave_accrual_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[LeaveAccrualLine]], FieldMetadata(alias="LeaveAccrualLines")
    ] = None
    leave_earnings_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[LeaveEarningsLine]], FieldMetadata(alias="LeaveEarningsLines")
    ] = None
    reimbursement_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[ReimbursementLine]], FieldMetadata(alias="ReimbursementLines")
    ] = None
    superannuation_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[SuperannuationLine]], FieldMetadata(alias="SuperannuationLines")
    ] = None
    tax_lines: typing_extensions.Annotated[typing.Optional[typing.List[TaxLine]], FieldMetadata(alias="TaxLines")] = (
        None
    )
    timesheet_earnings_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[EarningsLine]], FieldMetadata(alias="TimesheetEarningsLines")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
