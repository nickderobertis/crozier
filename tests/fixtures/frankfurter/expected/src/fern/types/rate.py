

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rate_providers_item import RateProvidersItem


class Rate(UniversalBaseModel):
    date: dt.date = pydantic.Field()
    """
    The date of the rate
    """

    base: str = pydantic.Field()
    """
    Base currency code
    """

    quote: str = pydantic.Field()
    """
    Quote currency code
    """

    rate: float = pydantic.Field()
    """
    Exchange rate value
    """

    providers: typing.Optional[typing.List[RateProvidersItem]] = pydantic.Field(default=None)
    """
    Per-provider rates for this pair. Present only when `expand=providers` is set. Each entry has the provider's observation date and published rate (rebased to the row's base). Entries with `excluded: true` did not contribute to the blended `rate` — either flagged as outliers by the consensus filter, or overridden by a currency peg. Omitted on synthesized peg rows where no provider published the quote.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
