

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deductions_breakdown import DeductionsBreakdown
from .deductions_total import DeductionsTotal
from .total import Total


class Deductions(UniversalBaseModel):
    """
    An object with the deduction information found on a paystub.
    """

    breakdown: typing.List[DeductionsBreakdown]
    subtotals: typing.Optional[typing.List[Total]] = None
    total: DeductionsTotal
    totals: typing.Optional[typing.List[Total]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
