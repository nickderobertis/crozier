

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Money(UniversalBaseModel):
    """

    Money fields can be signed or unsigned. Fields are signed (an unsigned value will be interpreted as positive). The amount of money will be represented in the smallest denomination
    of the currency indicated. For example, USD 7.00 will be represented in cents with an amount of 700.
    """

    amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    The amount of money, in the smallest denomination of the currency indicated by currency. For example, when currency is USD, amount is in cents.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of currency, in ISO 4217 format. Default to USD if not specified
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
