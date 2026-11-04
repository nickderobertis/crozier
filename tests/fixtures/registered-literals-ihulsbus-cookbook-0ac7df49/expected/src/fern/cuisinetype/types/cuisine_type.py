

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CuisineType(UniversalBaseModel):
    """
    Information about a Cuisine Type
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of a cuisine type
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    name of a cuisine type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
