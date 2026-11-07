

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Ingredient(UniversalBaseModel):
    """
    Returns information about an ingredient
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the ingredient
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the ingredient
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
