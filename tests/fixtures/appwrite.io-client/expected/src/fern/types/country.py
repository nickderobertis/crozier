

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Country(UniversalBaseModel):
    """
    Country
    """

    code: str = pydantic.Field()
    """
    Country two-character ISO 3166-1 alpha code.
    """

    name: str = pydantic.Field()
    """
    Country name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
