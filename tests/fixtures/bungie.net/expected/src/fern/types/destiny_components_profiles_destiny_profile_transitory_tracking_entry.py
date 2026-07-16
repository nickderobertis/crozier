

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyComponentsProfilesDestinyProfileTransitoryTrackingEntry(UniversalBaseModel):
    """
    This represents a single "thing" being tracked by the player.
    This can point to many types of entities, but only a subset of them will actually have a valid hash identifier for whatever it is being pointed to.
    It's up to you to interpret what it means when various combinations of these entries have values being tracked.
    """

    activity_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityHash"),
        pydantic.Field(
            alias="activityHash",
            description="OPTIONAL - If this is tracking the status of a DestinyActivityDefinition, this is the identifier for that activity.",
        ),
    ] = None
    """
    OPTIONAL - If this is tracking the status of a DestinyActivityDefinition, this is the identifier for that activity.
    """

    item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemHash"),
        pydantic.Field(
            alias="itemHash",
            description="OPTIONAL - If this is tracking the status of a DestinyInventoryItemDefinition, this is the identifier for that item.",
        ),
    ] = None
    """
    OPTIONAL - If this is tracking the status of a DestinyInventoryItemDefinition, this is the identifier for that item.
    """

    location_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="locationHash"),
        pydantic.Field(
            alias="locationHash",
            description="OPTIONAL - If this is tracking a DestinyLocationDefinition, this is the identifier for that location.",
        ),
    ] = None
    """
    OPTIONAL - If this is tracking a DestinyLocationDefinition, this is the identifier for that location.
    """

    objective_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="objectiveHash"),
        pydantic.Field(
            alias="objectiveHash",
            description="OPTIONAL - If this is tracking the status of a DestinyObjectiveDefinition, this is the identifier for that objective.",
        ),
    ] = None
    """
    OPTIONAL - If this is tracking the status of a DestinyObjectiveDefinition, this is the identifier for that objective.
    """

    questline_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="questlineItemHash"),
        pydantic.Field(
            alias="questlineItemHash",
            description="OPTIONAL - If this is tracking the status of a quest, this is the identifier for the DestinyInventoryItemDefinition that containst that questline data.",
        ),
    ] = None
    """
    OPTIONAL - If this is tracking the status of a quest, this is the identifier for the DestinyInventoryItemDefinition that containst that questline data.
    """

    tracked_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="trackedDate"),
        pydantic.Field(
            alias="trackedDate",
            description="OPTIONAL - I've got to level with you, I don't really know what this is. Is it when you started tracking it? Is it only populated for tracked items that have time limits?\r\nI don't know, but we can get at it - when I get time to actually test what it is, I'll update this. In the meantime, bask in the mysterious data.",
        ),
    ] = None
    """
    OPTIONAL - I've got to level with you, I don't really know what this is. Is it when you started tracking it? Is it only populated for tracked items that have time limits?
    I don't know, but we can get at it - when I get time to actually test what it is, I'll update this. In the meantime, bask in the mysterious data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
