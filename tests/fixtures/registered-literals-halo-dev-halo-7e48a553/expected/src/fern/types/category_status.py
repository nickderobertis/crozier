

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CategoryStatus(UniversalBaseModel):
    """
    Observed category state derived by content reconcilers.
    """

    permalink: typing.Optional[str] = pydantic.Field(default=None)
    """
    Absolute permalink calculated from the category permalink policy.
    """

    post_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="postCount"),
        pydantic.Field(
            alias="postCount", description="Total number of posts in this category and all descendant categories."
        ),
    ] = None
    """
    Total number of posts in this category and all descendant categories.
    """

    visible_post_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="visiblePostCount"),
        pydantic.Field(
            alias="visiblePostCount",
            description="Total number of published and public posts in this category and all descendant categories.",
        ),
    ] = None
    """
    Total number of published and public posts in this category and all descendant categories.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
