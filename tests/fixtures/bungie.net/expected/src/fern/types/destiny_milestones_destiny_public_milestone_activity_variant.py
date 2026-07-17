

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyMilestonesDestinyPublicMilestoneActivityVariant(UniversalBaseModel):
    """
    Represents a variant of an activity that's relevant to a milestone.
    """

    activity_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityHash"),
        pydantic.Field(
            alias="activityHash",
            description="The hash identifier of this activity variant. Examine the activity's definition in the Manifest database to determine what makes it a distinct variant. Usually it will be difficulty level or whether or not it is a guided game variant of the activity, but theoretically it could be distinguished in any arbitrary way.",
        ),
    ] = None
    """
    The hash identifier of this activity variant. Examine the activity's definition in the Manifest database to determine what makes it a distinct variant. Usually it will be difficulty level or whether or not it is a guided game variant of the activity, but theoretically it could be distinguished in any arbitrary way.
    """

    activity_mode_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityModeHash"),
        pydantic.Field(
            alias="activityModeHash",
            description="The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way.",
        ),
    ] = None
    """
    The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way.
    """

    activity_mode_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityModeType"),
        pydantic.Field(
            alias="activityModeType",
            description="The enumeration equivalent of the most specific Activity Mode under which this activity is played.",
        ),
    ] = None
    """
    The enumeration equivalent of the most specific Activity Mode under which this activity is played.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
