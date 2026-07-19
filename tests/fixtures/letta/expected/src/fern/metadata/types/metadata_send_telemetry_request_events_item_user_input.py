

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metadata_send_telemetry_request_events_item_user_input_data import (
    MetadataSendTelemetryRequestEventsItemUserInputData,
)


class MetadataSendTelemetryRequestEventsItemUserInput(UniversalBaseModel):
    timestamp: str
    data: MetadataSendTelemetryRequestEventsItemUserInputData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
