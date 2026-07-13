

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount


class CurrencyConversionQuoteRead(UniversalBaseModel):
    amount_source: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount to convert.
    """

    amount_target: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount to convert to.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the quote's creation.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the quote.
    """

    rate: typing.Optional[str] = pydantic.Field(default=None)
    """
    The conversion rate.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the quote.
    """

    time_expiry: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timestamp for when this quote expires and the user should request a new one.
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
