

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pay_stub_earnings_breakdown import PayStubEarningsBreakdown
from .pay_stub_earnings_total import PayStubEarningsTotal


class CreditPayStubEarnings(UniversalBaseModel):
    """
    An object representing both a breakdown of earnings on a pay stub and the total earnings.
    """

    breakdown: typing.List[PayStubEarningsBreakdown]
    total: PayStubEarningsTotal

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
