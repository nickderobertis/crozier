

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PodcastMetadata(UniversalBaseModel):
    """
    Metadata for a podcast.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the podcast.
    """

    author: typing.Optional[str] = pydantic.Field(default=None)
    """
    The author of the podcast.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the podcast.
    """

    release_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="releaseDate"),
        pydantic.Field(alias="releaseDate", description="The release date of the podcast."),
    ] = None
    """
    The release date of the podcast.
    """

    genres: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The genres of the podcast.
    """

    feed_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="feedUrl"),
        pydantic.Field(alias="feedUrl", description="The URL of the podcast feed."),
    ] = None
    """
    The URL of the podcast feed.
    """

    image_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="imageUrl"),
        pydantic.Field(alias="imageUrl", description="The URL of the podcast's image."),
    ] = None
    """
    The URL of the podcast's image.
    """

    itunes_page_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itunesPageUrl"),
        pydantic.Field(alias="itunesPageUrl", description="The URL of the podcast's iTunes page."),
    ] = None
    """
    The URL of the podcast's iTunes page.
    """

    itunes_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itunesId"),
        pydantic.Field(alias="itunesId", description="The iTunes ID of the podcast."),
    ] = None
    """
    The iTunes ID of the podcast.
    """

    itunes_artist_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itunesArtistId"),
        pydantic.Field(alias="itunesArtistId", description="The iTunes artist ID of the podcast."),
    ] = None
    """
    The iTunes artist ID of the podcast.
    """

    explicit: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the podcast contains explicit content.
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The language of the podcast.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of podcast (e.g., episodic, serial).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
