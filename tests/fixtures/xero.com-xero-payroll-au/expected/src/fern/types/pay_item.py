

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .deduction_type import DeductionType
from .earnings_rate import EarningsRate
from .leave_type import LeaveType
from .reimbursement_type import ReimbursementType


class PayItem(UniversalBaseModel):
    deduction_types: typing_extensions.Annotated[
        typing.Optional[typing.List[DeductionType]],
        FieldMetadata(alias="DeductionTypes"),
        pydantic.Field(alias="DeductionTypes"),
    ] = None
    earnings_rates: typing_extensions.Annotated[
        typing.Optional[typing.List[EarningsRate]],
        FieldMetadata(alias="EarningsRates"),
        pydantic.Field(alias="EarningsRates"),
    ] = None
    leave_types: typing_extensions.Annotated[
        typing.Optional[typing.List[LeaveType]], FieldMetadata(alias="LeaveTypes"), pydantic.Field(alias="LeaveTypes")
    ] = None
    reimbursement_types: typing_extensions.Annotated[
        typing.Optional[typing.List[ReimbursementType]],
        FieldMetadata(alias="ReimbursementTypes"),
        pydantic.Field(alias="ReimbursementTypes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
