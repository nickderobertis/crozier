

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetadataSearchResponse(UniversalBaseModel):
    """
    Response on a metadata search request
    """

    recipe_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    UUID of the recipe
    """

    category_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Array with category UUIDs belonging to the recipe
    """

    tag_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Array with tag UUIDs belonging to the recipe
    """

    difficulty_level_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    UUID of the difficulty level associated to a recipe
    """

    preparation_time_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    UUID of the preparation time associated to a recipe
    """

    cuisine_type_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    UUID of the cuisine type associated to a recipe
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
