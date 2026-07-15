

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Continent(UniversalBaseModel):
    """
    Continent
    """

    code: str = pydantic.Field()
    """
    Continent two letter code.
    """

    name: str = pydantic.Field()
    """
    Continent name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
