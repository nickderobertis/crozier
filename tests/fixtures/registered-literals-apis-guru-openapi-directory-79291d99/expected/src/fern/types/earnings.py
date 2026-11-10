

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .earnings_breakdown import EarningsBreakdown
from .earnings_total import EarningsTotal


class Earnings(UniversalBaseModel):
    """
    An object representing both a breakdown of earnings on a paystub and the total earnings.
    """

    breakdown: typing.Optional[typing.List[EarningsBreakdown]] = None
    subtotals: typing.Optional[typing.List[EarningsTotal]] = None
    total: typing.Optional[EarningsTotal] = None
    totals: typing.Optional[typing.List[EarningsTotal]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
