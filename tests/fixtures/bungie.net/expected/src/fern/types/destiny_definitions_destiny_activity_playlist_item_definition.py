

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyActivityPlaylistItemDefinition(UniversalBaseModel):
    """
    If the activity is a playlist, this is the definition for a specific entry in the playlist: a single possible combination of Activity and Activity Mode that can be chosen.
    """

    activity_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityHash"),
        pydantic.Field(
            alias="activityHash",
            description="The hash identifier of the Activity that can be played. Use it to look up the DestinyActivityDefinition.",
        ),
    ] = None
    """
    The hash identifier of the Activity that can be played. Use it to look up the DestinyActivityDefinition.
    """

    activity_mode_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="activityModeHashes"),
        pydantic.Field(
            alias="activityModeHashes", description="The hash identifiers for Activity Modes relevant to this entry."
        ),
    ] = None
    """
    The hash identifiers for Activity Modes relevant to this entry.
    """

    activity_mode_types: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="activityModeTypes"),
        pydantic.Field(
            alias="activityModeTypes",
            description="The activity modes - if any - in enum form. Because we can't seem to escape the enums.",
        ),
    ] = None
    """
    The activity modes - if any - in enum form. Because we can't seem to escape the enums.
    """

    direct_activity_mode_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="directActivityModeHash"),
        pydantic.Field(
            alias="directActivityModeHash",
            description="If this playlist entry had an activity mode directly defined on it, this will be the hash of that mode.",
        ),
    ] = None
    """
    If this playlist entry had an activity mode directly defined on it, this will be the hash of that mode.
    """

    direct_activity_mode_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="directActivityModeType"),
        pydantic.Field(
            alias="directActivityModeType",
            description="If the playlist entry had an activity mode directly defined on it, this will be the enum value of that mode.",
        ),
    ] = None
    """
    If the playlist entry had an activity mode directly defined on it, this will be the enum value of that mode.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
