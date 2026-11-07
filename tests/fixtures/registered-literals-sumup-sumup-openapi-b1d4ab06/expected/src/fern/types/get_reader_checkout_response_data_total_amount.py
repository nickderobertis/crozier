

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetReaderCheckoutResponseDataTotalAmount(UniversalBaseModel):
    """
    Amount structure.

    The amount is represented as an integer value altogether with the currency and the minor unit.

    For example, EUR 1.00 is represented as value 100 with minor unit of 2.
    """

    currency: str = pydantic.Field()
    """
    Currency ISO 4217 code
    """

    minor_unit: int = pydantic.Field()
    """
    The minor units of the currency.
    It represents the number of decimals of the currency. For the currencies CLP, COP and HUF, the minor unit is 0.
    """

    value: int = pydantic.Field()
    """
    Integer value of the amount.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
