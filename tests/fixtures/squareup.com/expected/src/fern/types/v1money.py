

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1Money(UniversalBaseModel):
    """ """

    amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    Amount in the lowest denominated value of this Currency. E.g. in USD
    these are cents, in JPY they are Yen (which do not have a 'cent' concept).
    """

    currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
