

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class TrendingTrendingEntry(UniversalBaseModel):
    """
    The list entry view for trending items. Returns just enough to show the item on the trending page.
    """

    creation_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="creationDate"),
        pydantic.Field(
            alias="creationDate", description="If the entry has a date at which it was created, this is that date."
        ),
    ] = None
    """
    If the entry has a date at which it was created, this is that date.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(
            alias="displayName",
            description="The localized \"display name/article title/'primary localized identifier'\" of the entity.",
        ),
    ] = None
    """
    The localized "display name/article title/'primary localized identifier'" of the entity.
    """

    end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="endDate"), pydantic.Field(alias="endDate")
    ] = None
    entity_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="entityType"),
        pydantic.Field(
            alias="entityType",
            description="An enum - unfortunately - dictating all of the possible kinds of trending items that you might get in your result set, in case you want to do custom rendering or call to get the details of the item.",
        ),
    ] = None
    """
    An enum - unfortunately - dictating all of the possible kinds of trending items that you might get in your result set, in case you want to do custom rendering or call to get the details of the item.
    """

    feature_image: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="featureImage"),
        pydantic.Field(
            alias="featureImage",
            description="If isFeatured, this image will be populated with whatever the featured image is. Note that this will likely be a very large image, so don't use it all the time.",
        ),
    ] = None
    """
    If isFeatured, this image will be populated with whatever the featured image is. Note that this will likely be a very large image, so don't use it all the time.
    """

    identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    We don't know whether the identifier will be a string, a uint, or a long... so we're going to cast it all to a string. But either way, we need any trending item created to have a single unique identifier for its type.
    """

    image: typing.Optional[str] = None
    is_featured: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isFeatured"), pydantic.Field(alias="isFeatured")
    ] = None
    items: typing.Optional[typing.List["TrendingTrendingEntry"]] = pydantic.Field(default=None)
    """
    If the item is of entityType TrendingEntryType.Container, it may have items - also Trending Entries - contained within it. This is the ordered list of those to display under the Container's header.
    """

    link: typing.Optional[str] = None
    mp4video: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mp4Video"),
        pydantic.Field(
            alias="mp4Video",
            description="If this is populated, the entry has a related MP4 video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo",
        ),
    ] = None
    """
    If this is populated, the entry has a related MP4 video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo
    """

    start_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startDate"), pydantic.Field(alias="startDate")
    ] = None
    tagline: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the entity has a localized tagline/subtitle/motto/whatever, that is found here.
    """

    webm_video: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="webmVideo"),
        pydantic.Field(
            alias="webmVideo",
            description="If this is populated, the entry has a related WebM video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo",
        ),
    ] = None
    """
    If this is populated, the entry has a related WebM video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo
    """

    weight: typing.Optional[float] = pydantic.Field(default=None)
    """
    The weighted score of this trending item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(TrendingTrendingEntry)
