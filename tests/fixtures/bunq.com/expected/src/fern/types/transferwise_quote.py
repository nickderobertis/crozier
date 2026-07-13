

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount


class TransferwiseQuote(UniversalBaseModel):
    amount_fee: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The fee amount.
    """

    amount_source: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The source amount.
    """

    amount_target: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The target amount.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the quote's creation.
    """

    currency_source: str = pydantic.Field()
    """
    The source currency.
    """

    currency_target: str = pydantic.Field()
    """
    The target currency.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the quote.
    """

    quote_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The quote id Transferwise needs.
    """

    rate: typing.Optional[str] = pydantic.Field(default=None)
    """
    The rate.
    """

    time_delivery_estimate: typing.Optional[str] = pydantic.Field(default=None)
    """
    The estimated delivery time.
    """

    time_expiry: typing.Optional[str] = pydantic.Field(default=None)
    """
    The expiration timestamp of the quote.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the quote's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
