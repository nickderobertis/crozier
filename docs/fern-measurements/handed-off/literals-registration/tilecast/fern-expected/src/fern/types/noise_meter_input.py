

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .noise_meter_input_display_mode import NoiseMeterInputDisplayMode
from .noise_meter_input_target_scope import NoiseMeterInputTargetScope


class NoiseMeterInput(UniversalBaseModel):
    """
    Thresholds for the Linux Player's room noise bar. Levels are a relative 0-100 scale measured against that player's own microphone; they are not dB, dBA, or SPL, and no audio, sample, or microphone identifier is exchanged in either direction. warningLevel must be below loudLevel: one threshold used for both showing and hiding makes the bar flap.
    """

    name: str
    message: str = pydantic.Field()
    """
    Replaces the bar's own TOO LOUD label. Empty is allowed.
    """

    warning_level: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="warningLevel"),
        pydantic.Field(
            alias="warningLevel",
            description="Where the yellow zone begins, and the level the room must stay below before the bar hides.",
        ),
    ]
    """
    Where the yellow zone begins, and the level the room must stay below before the bar hides.
    """

    loud_level: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="loudLevel"),
        pydantic.Field(alias="loudLevel", description="Where the red zone begins and the bar can appear."),
    ]
    """
    Where the red zone begins and the bar can appear.
    """

    sensitivity: int = pydantic.Field()
    """
    Percentage applied to the captured signal before normalization, for a microphone that reads quiet or hot. Not a calibration.
    """

    trigger_hold_ms: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="triggerHoldMs"),
        pydantic.Field(alias="triggerHoldMs", description="How long the room must stay loud before the bar appears."),
    ]
    """
    How long the room must stay loud before the bar appears.
    """

    clear_hold_ms: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="clearHoldMs"),
        pydantic.Field(
            alias="clearHoldMs", description="How long it must stay below warningLevel before the bar hides."
        ),
    ]
    """
    How long it must stay below warningLevel before the bar hides.
    """

    display_mode: typing_extensions.Annotated[
        NoiseMeterInputDisplayMode, FieldMetadata(alias="displayMode"), pydantic.Field(alias="displayMode")
    ]
    height_px: typing_extensions.Annotated[int, FieldMetadata(alias="heightPx"), pydantic.Field(alias="heightPx")]
    schedule_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="scheduleEnabled"),
        pydantic.Field(
            alias="scheduleEnabled",
            description="When false the bar may show whenever the room is too loud. A window governs the bar alone; the room is measured either way.",
        ),
    ] = None
    """
    When false the bar may show whenever the room is too loud. A window governs the bar alone; the room is measured either way.
    """

    schedule_days_of_week: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="scheduleDaysOfWeek"),
        pydantic.Field(
            alias="scheduleDaysOfWeek", description="Days the window may start on, Sunday 0 through Saturday 6."
        ),
    ] = None
    """
    Days the window may start on, Sunday 0 through Saturday 6.
    """

    schedule_start_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="scheduleStartTime"), pydantic.Field(alias="scheduleStartTime")
    ] = None
    schedule_end_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="scheduleEndTime"),
        pydantic.Field(
            alias="scheduleEndTime",
            description="At or before the start is an overnight window belonging to the start day. The window is half-open, so the end minute is outside it.",
        ),
    ] = None
    """
    At or before the start is an overnight window belonging to the start day. The window is half-open, so the end minute is outside it.
    """

    schedule_timezone: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="scheduleTimezone"), pydantic.Field(alias="scheduleTimezone")
    ] = None
    enabled: bool
    target_scope: typing_extensions.Annotated[
        NoiseMeterInputTargetScope, FieldMetadata(alias="targetScope"), pydantic.Field(alias="targetScope")
    ]
    target_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="targetIds"), pydantic.Field(alias="targetIds")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
