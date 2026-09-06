

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ListCollectionsResponseCollectionsItem(UniversalBaseModel):
    """
    A collection object
    """

    id: str = pydantic.Field()
    """
    Unique identifier for a Collection
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Name given to the Collection"),
    ] = None
    """
    Name given to the Collection
    """

    singular_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="singularName"),
        pydantic.Field(
            alias="singularName",
            description="The name of one Item in Collection (e.g. ”Blog Post” if the Collection is called “Blog Posts”)",
        ),
    ] = None
    """
    The name of one Item in Collection (e.g. ”Blog Post” if the Collection is called “Blog Posts”)
    """

    slug: typing.Optional[str] = pydantic.Field(default=None)
    """
    Slug of Collection in Site URL structure
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="The date the collection was created"),
    ] = None
    """
    The date the collection was created
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="The date the collection was last updated"),
    ] = None
    """
    The date the collection was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
