

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PageMetadataAttributes(UniversalBaseModel):
    """
    SEO fields held by one page-metadata entry (one per site route).
    """

    page_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pagePath"),
        pydantic.Field(alias="pagePath", description="Site route this metadata applies to (e.g. /apis/{slug})."),
    ] = None
    """
    Site route this metadata applies to (e.g. /apis/{slug}).
    """

    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    robots_index: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="robotsIndex"),
        pydantic.Field(alias="robotsIndex", description="Whether the route may be indexed (drives sitemap inclusion)."),
    ] = None
    """
    Whether the route may be indexed (drives sitemap inclusion).
    """

    robots_follow: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="robotsFollow"),
        pydantic.Field(alias="robotsFollow", description="Whether links on the route may be followed."),
    ] = None
    """
    Whether links on the route may be followed.
    """

    og_title: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ogTitle"), pydantic.Field(alias="ogTitle")
    ] = None
    og_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ogDescription"), pydantic.Field(alias="ogDescription")
    ] = None
    og_image: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ogImage"), pydantic.Field(alias="ogImage")
    ] = None
    twitter_title: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="twitterTitle"), pydantic.Field(alias="twitterTitle")
    ] = None
    twitter_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="twitterDescription"), pydantic.Field(alias="twitterDescription")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
