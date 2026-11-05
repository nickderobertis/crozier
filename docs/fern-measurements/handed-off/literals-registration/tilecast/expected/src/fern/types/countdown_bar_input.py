

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .countdown_bar_input_display_mode import CountdownBarInputDisplayMode
from .countdown_bar_input_progress_fill import CountdownBarInputProgressFill
from .countdown_bar_input_schedule_type import CountdownBarInputScheduleType
from .countdown_bar_input_target_scope import CountdownBarInputTargetScope


class CountdownBarInput(UniversalBaseModel):
    name: str
    message: str
    schedule_type: typing_extensions.Annotated[
        CountdownBarInputScheduleType, FieldMetadata(alias="scheduleType"), pydantic.Field(alias="scheduleType")
    ]
    target_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetTime"), pydantic.Field(alias="targetTime")
    ] = None
    days_of_week: typing_extensions.Annotated[
        typing.List[int], FieldMetadata(alias="daysOfWeek"), pydantic.Field(alias="daysOfWeek")
    ]
    one_time_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="oneTimeAt"), pydantic.Field(alias="oneTimeAt")
    ] = None
    timezone: str
    lead_time_seconds: typing_extensions.Annotated[
        int, FieldMetadata(alias="leadTimeSeconds"), pydantic.Field(alias="leadTimeSeconds")
    ]
    completion_text: typing_extensions.Annotated[
        str, FieldMetadata(alias="completionText"), pydantic.Field(alias="completionText")
    ]
    show_confetti: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="showConfetti"),
        pydantic.Field(
            alias="showConfetti",
            description="Show a short confetti fall from the top of the Player when the countdown reaches zero. This does not require completion text.",
        ),
    ]
    """
    Show a short confetti fall from the top of the Player when the countdown reaches zero. This does not require completion text.
    """

    display_mode: typing_extensions.Annotated[
        CountdownBarInputDisplayMode, FieldMetadata(alias="displayMode"), pydantic.Field(alias="displayMode")
    ]
    height_px: typing_extensions.Annotated[int, FieldMetadata(alias="heightPx"), pydantic.Field(alias="heightPx")]
    progress_fill: typing_extensions.Annotated[
        typing.Optional[CountdownBarInputProgressFill],
        FieldMetadata(alias="progressFill"),
        pydantic.Field(
            alias="progressFill",
            description='Background treatment behind the bar text. "drain" starts the bar fully tinted when the lead window opens and retreats the tint leftward as the target approaches, leaving only the bar background at zero. Omitted means "none".',
        ),
    ] = None
    """
    Background treatment behind the bar text. "drain" starts the bar fully tinted when the lead window opens and retreats the tint leftward as the target approaches, leaving only the bar background at zero. Omitted means "none".
    """

    content_padding: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="contentPadding"),
        pydantic.Field(
            alias="contentPadding",
            description="Share of each side left as a gutter, as a percentage of the bar width. Lowering it gives a long message or a larger type size more room. The default 4 matches the bar's original gutters.",
        ),
    ] = None
    """
    Share of each side left as a gutter, as a percentage of the bar width. Lowering it gives a long message or a larger type size more room. The default 4 matches the bar's original gutters.
    """

    text_scale: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="textScale"),
        pydantic.Field(
            alias="textScale",
            description="Percentage applied to the height-derived type size, so a bar can carry larger text without changing its height. 100 is the original appearance.",
        ),
    ] = None
    """
    Percentage applied to the height-derived type size, so a bar can carry larger text without changing its height. 100 is the original appearance.
    """

    urgency_enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="urgencyEnabled"),
        pydantic.Field(
            alias="urgencyEnabled", description="Enable automatic starting-soon, urgent, and final pulse stages."
        ),
    ]
    """
    Enable automatic starting-soon, urgent, and final pulse stages.
    """

    starting_soon_seconds: typing_extensions.Annotated[
        int, FieldMetadata(alias="startingSoonSeconds"), pydantic.Field(alias="startingSoonSeconds")
    ]
    urgent_seconds: typing_extensions.Annotated[
        int, FieldMetadata(alias="urgentSeconds"), pydantic.Field(alias="urgentSeconds")
    ]
    pulse_seconds: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="pulseSeconds"),
        pydantic.Field(
            alias="pulseSeconds",
            description="Final seconds during which the urgent bar pulses and grows by 25 percent.",
        ),
    ]
    """
    Final seconds during which the urgent bar pulses and grows by 25 percent.
    """

    enabled: bool
    priority: int
    target_scope: typing_extensions.Annotated[
        CountdownBarInputTargetScope, FieldMetadata(alias="targetScope"), pydantic.Field(alias="targetScope")
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
