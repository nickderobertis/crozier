

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metadata_send_telemetry_request_events_item_error_data import MetadataSendTelemetryRequestEventsItemErrorData
from .metadata_send_telemetry_request_events_item_session_end_data import (
    MetadataSendTelemetryRequestEventsItemSessionEndData,
)
from .metadata_send_telemetry_request_events_item_session_start_data import (
    MetadataSendTelemetryRequestEventsItemSessionStartData,
)
from .metadata_send_telemetry_request_events_item_tool_usage_data import (
    MetadataSendTelemetryRequestEventsItemToolUsageData,
)
from .metadata_send_telemetry_request_events_item_user_input_data import (
    MetadataSendTelemetryRequestEventsItemUserInputData,
)


class MetadataSendTelemetryRequestEventsItem_SessionStart(UniversalBaseModel):
    type: typing.Literal["session_start"] = "session_start"
    timestamp: str
    data: MetadataSendTelemetryRequestEventsItemSessionStartData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MetadataSendTelemetryRequestEventsItem_SessionEnd(UniversalBaseModel):
    type: typing.Literal["session_end"] = "session_end"
    timestamp: str
    data: MetadataSendTelemetryRequestEventsItemSessionEndData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MetadataSendTelemetryRequestEventsItem_ToolUsage(UniversalBaseModel):
    type: typing.Literal["tool_usage"] = "tool_usage"
    timestamp: str
    data: MetadataSendTelemetryRequestEventsItemToolUsageData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MetadataSendTelemetryRequestEventsItem_Error(UniversalBaseModel):
    type: typing.Literal["error"] = "error"
    timestamp: str
    data: MetadataSendTelemetryRequestEventsItemErrorData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class MetadataSendTelemetryRequestEventsItem_UserInput(UniversalBaseModel):
    type: typing.Literal["user_input"] = "user_input"
    timestamp: str
    data: MetadataSendTelemetryRequestEventsItemUserInputData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


MetadataSendTelemetryRequestEventsItem = typing_extensions.Annotated[
    typing.Union[
        MetadataSendTelemetryRequestEventsItem_SessionStart,
        MetadataSendTelemetryRequestEventsItem_SessionEnd,
        MetadataSendTelemetryRequestEventsItem_ToolUsage,
        MetadataSendTelemetryRequestEventsItem_Error,
        MetadataSendTelemetryRequestEventsItem_UserInput,
    ],
    pydantic.Field(discriminator="type"),
]
