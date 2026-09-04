

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Amount(UniversalBaseModel):
    currency: str = pydantic.Field()
    """
    The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount.
    """

    value: int = pydantic.Field()
    """
    The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
