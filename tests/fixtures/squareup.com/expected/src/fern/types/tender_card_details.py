

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .card import Card


class TenderCardDetails(UniversalBaseModel):
    """
    Represents additional details of a tender with `type` `CARD` or `SQUARE_GIFT_CARD`
    """

    card: typing.Optional[Card] = None
    entry_method: typing.Optional[str] = pydantic.Field(default=None)
    """
    The method used to enter the card's details for the transaction.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The credit card payment's current state (such as `AUTHORIZED` or
    `CAPTURED`). See [TenderCardDetailsStatus](https://developer.squareup.com/reference/square_2021-08-18/objects/TenderCardDetailsStatus)
    for possible values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
