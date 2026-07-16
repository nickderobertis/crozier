

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_seasons_destiny_season_preview_definition import (
    DestinyDefinitionsSeasonsDestinySeasonPreviewDefinition,
)


class DestinyDefinitionsSeasonsDestinySeasonDefinition(UniversalBaseModel):
    """
    Defines a canonical "Season" of Destiny: a range of a few months where the game highlights certain challenges, provides new loot, has new Clan-related rewards and celebrates various seasonal events.
    """

    artifact_item_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="artifactItemHash"), pydantic.Field(alias="artifactItemHash")
    ] = None
    background_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="backgroundImagePath"), pydantic.Field(alias="backgroundImagePath")
    ] = None
    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties"),
    ] = None
    end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="endDate"), pydantic.Field(alias="endDate")
    ] = None
    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    preview: typing.Optional[DestinyDefinitionsSeasonsDestinySeasonPreviewDefinition] = pydantic.Field(default=None)
    """
    Optional - Defines the promotional text, images, and links to preview this season.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    seal_presentation_node_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sealPresentationNodeHash"),
        pydantic.Field(alias="sealPresentationNodeHash"),
    ] = None
    season_number: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="seasonNumber"), pydantic.Field(alias="seasonNumber")
    ] = None
    season_pass_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="seasonPassHash"), pydantic.Field(alias="seasonPassHash")
    ] = None
    season_pass_progression_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="seasonPassProgressionHash"),
        pydantic.Field(alias="seasonPassProgressionHash"),
    ] = None
    seasonal_challenges_presentation_node_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="seasonalChallengesPresentationNodeHash"),
        pydantic.Field(alias="seasonalChallengesPresentationNodeHash"),
    ] = None
    start_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startDate"), pydantic.Field(alias="startDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
