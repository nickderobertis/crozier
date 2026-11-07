

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Amount(UniversalBaseModel):
    currency: str = pydantic.Field()
    """
    Currency ISO 4217 code
    """

    value: int = pydantic.Field()
    """
    Amount in minor units (e.g. cents).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
