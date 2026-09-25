

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Amount(UniversalBaseModel):
    net: float = pydantic.Field()
    """
    Net amount in minor units
    """

    gross: float = pydantic.Field()
    """
    Gross amount in minor units
    """

    tax: float = pydantic.Field()
    """
    Tax amount in minor units
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
