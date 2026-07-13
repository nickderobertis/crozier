

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_seasons_destiny_season_preview_image_definition import (
    DestinyDefinitionsSeasonsDestinySeasonPreviewImageDefinition,
)


class DestinyDefinitionsSeasonsDestinySeasonPreviewDefinition(UniversalBaseModel):
    """
    Defines the promotional text, images, and links to preview this season.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A localized description of the season.
    """

    images: typing.Optional[typing.List[DestinyDefinitionsSeasonsDestinySeasonPreviewImageDefinition]] = pydantic.Field(
        default=None
    )
    """
    A list of images to preview the seasonal content. Should have at least three to show.
    """

    link_path: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="linkPath")] = pydantic.Field(
        default=None
    )
    """
    A relative path to learn more about the season. Web browsers should be automatically redirected to the user's Bungie.net locale. For example: "/SeasonOfTheChosen" will redirect to "/7/en/Seasons/SeasonOfTheChosen" for English users.
    """

    video_link: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="videoLink")] = pydantic.Field(
        default=None
    )
    """
    An optional link to a localized video, probably YouTube.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
