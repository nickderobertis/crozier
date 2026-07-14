

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency import Currency


class CurrencyList(UniversalBaseModel):
    """
    Currencies List
    """

    currencies: typing.List[Currency] = pydantic.Field()
    """
    List of currencies.
    """

    sum: int = pydantic.Field()
    """
    Total sum of items in the list.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
