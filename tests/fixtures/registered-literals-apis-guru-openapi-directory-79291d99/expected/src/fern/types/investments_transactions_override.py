

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .security_override import SecurityOverride


class InvestmentsTransactionsOverride(UniversalBaseModel):
    """
    Specify the list of investments transactions on the account.
    """

    currency: str = pydantic.Field()
    """
    Either a valid `iso_currency_code` or `unofficial_currency_code`
    """

    date: dt.date = pydantic.Field()
    """
    Posting date for the transaction. Must be formatted as an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) date.
    """

    fees: typing.Optional[float] = pydantic.Field(default=None)
    """
    The combined value of all fees applied to this transaction.
    """

    name: str = pydantic.Field()
    """
    The institution's description of the transaction.
    """

    price: float = pydantic.Field()
    """
    The price of the security at which this transaction occurred.
    """

    quantity: float = pydantic.Field()
    """
    The number of units of the security involved in this transaction. Must be positive if the type is a buy and negative if the type is a sell.
    """

    security: typing.Optional[SecurityOverride] = None
    type: str = pydantic.Field()
    """
    The type of the investment transaction. Possible values are:
    `buy`: Buying an investment
    `sell`: Selling an investment
    `cash`: Activity that modifies a cash position
    `fee`: A fee on the account
    `transfer`: Activity that modifies a position, but not through buy/sell activity e.g. options exercise, portfolio transfer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
