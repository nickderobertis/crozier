

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .abstract_exchange_type import AbstractExchangeType


class AbstractExchange(UniversalBaseModel):
    """
    Abstract bean representing a Service or API Exchange.
    """

    type: AbstractExchangeType = pydantic.Field()
    """
    Discriminant type for identifying kind of exchange
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
