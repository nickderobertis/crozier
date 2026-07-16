

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .deduction_line import DeductionLine
from .earnings_line import EarningsLine
from .leave_line import LeaveLine
from .reimbursement_line import ReimbursementLine
from .super_line import SuperLine


class OpeningBalances(UniversalBaseModel):
    deduction_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[DeductionLine]], FieldMetadata(alias="DeductionLines")
    ] = None
    earnings_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[EarningsLine]], FieldMetadata(alias="EarningsLines")
    ] = None
    leave_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[LeaveLine]], FieldMetadata(alias="LeaveLines")
    ] = None
    opening_balance_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="OpeningBalanceDate")
    ] = pydantic.Field(default=None)
    """
    Opening Balance Date. (YYYY-MM-DD)
    """

    reimbursement_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[ReimbursementLine]], FieldMetadata(alias="ReimbursementLines")
    ] = None
    super_lines: typing_extensions.Annotated[
        typing.Optional[typing.List[SuperLine]], FieldMetadata(alias="SuperLines")
    ] = None
    tax: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Tax")] = pydantic.Field(default=None)
    """
    Opening Balance tax
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
