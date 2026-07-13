

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .pointer import Pointer


class CurrencyConversionQuote(UniversalBaseModel):
    amount: Amount = pydantic.Field()
    """
    The amount to convert.
    """

    counterparty_alias: Pointer = pydantic.Field()
    """
    The Alias of the party we are transferring the money to.
    """

    currency_source: str = pydantic.Field()
    """
    The currency we are converting.
    """

    currency_target: str = pydantic.Field()
    """
    The currency we are converting towards.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the quote.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
