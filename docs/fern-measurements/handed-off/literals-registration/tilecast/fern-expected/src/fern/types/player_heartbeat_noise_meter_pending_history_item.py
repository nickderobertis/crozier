

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PlayerHeartbeatNoiseMeterPendingHistoryItem(UniversalBaseModel):
    started_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startedAt"),
        pydantic.Field(alias="startedAt", description="Start of the fixed ten-second grid slot."),
    ]
    """
    Start of the fixed ten-second grid slot.
    """

    average_level: typing_extensions.Annotated[
        float, FieldMetadata(alias="averageLevel"), pydantic.Field(alias="averageLevel")
    ]
    peak_level: typing_extensions.Annotated[float, FieldMetadata(alias="peakLevel"), pydantic.Field(alias="peakLevel")]
    monitored_ms: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monitoredMs"),
        pydantic.Field(
            alias="monitoredMs",
            description="How much of the bucket the microphone actually covered, so a partly monitored slot is not read as ten seconds of quiet.",
        ),
    ]
    """
    How much of the bucket the microphone actually covered, so a partly monitored slot is not read as ten seconds of quiet.
    """

    warning_ms: typing_extensions.Annotated[int, FieldMetadata(alias="warningMs"), pydantic.Field(alias="warningMs")]
    loud_ms: typing_extensions.Annotated[int, FieldMetadata(alias="loudMs"), pydantic.Field(alias="loudMs")]
    trigger_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="triggerCount"),
        pydantic.Field(
            alias="triggerCount",
            description="Times the Player's state machine entered its loud state in this bucket, counted where it happened.",
        ),
    ] = None
    """
    Times the Player's state machine entered its loud state in this bucket, counted where it happened.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
