

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency import Currency


class MessagePrice(UniversalBaseModel):
    """
    Price of the message.
    """

    currency: typing.Optional[Currency] = None
    per_unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    total_amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
