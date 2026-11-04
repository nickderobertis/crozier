

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CategorySpec(UniversalBaseModel):
    """
    Desired category display, hierarchy, and rendering configuration.
    """

    children: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Legacy child Category metadata.name values. Category hierarchy is now sourced from Category.spec.parent.
    """

    cover: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cover image URL or attachment URI of the category.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description of the category.
    """

    display_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name of the category."),
    ]
    """
    Display name of the category.
    """

    hide_from_list: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hideFromList"),
        pydantic.Field(
            alias="hideFromList",
            description="Hides this root category tree and its posts from theme-side lists. Permalinks remain accessible, and only\n root categories are expected to set this flag.",
        ),
    ] = None
    """
    Hides this root category tree and its posts from theme-side lists. Permalinks remain accessible, and only
     root categories are expected to set this flag.
    """

    parent: typing.Optional[str] = pydantic.Field(default=None)
    """
    Parent Category metadata.name. Root categories leave this unset.
    """

    post_template: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="postTemplate"),
        pydantic.Field(
            alias="postTemplate",
            description="Theme template used for posts in this category when the post does not specify its own spec.template.",
        ),
    ] = None
    """
    Theme template used for posts in this category when the post does not specify its own spec.template.
    """

    prevent_parent_post_cascade_query: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="preventParentPostCascadeQuery"),
        pydantic.Field(
            alias="preventParentPostCascadeQuery",
            description="Stops parent category post queries from cascading into this category tree. Direct post queries for this\n category are unaffected.",
        ),
    ] = None
    """
    Stops parent category post queries from cascading into this category tree. Direct post queries for this
     category are unaffected.
    """

    priority: int = pydantic.Field()
    """
    Sorting priority. Higher values sort before lower values where priority ordering is applied.
    """

    slug: str = pydantic.Field()
    """
    URL slug used to build the category permalink.
    """

    template: typing.Optional[str] = pydantic.Field(default=None)
    """
    Theme template used to render the category archive page.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
