

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Recipe(UniversalBaseModel):
    """
    Definition of a recipe
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of a recipe
    """

    name: str = pydantic.Field()
    """
    Name of a recipe
    """

    description: str = pydantic.Field()
    """
    Short description of the recipe
    """

    serving_count: int = pydantic.Field()
    """
    amount of servings a recipe makes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
