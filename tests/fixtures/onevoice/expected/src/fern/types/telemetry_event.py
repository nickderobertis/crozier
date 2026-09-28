

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .telemetry_event_event_type import TelemetryEventEventType


class TelemetryEvent(UniversalBaseModel):
    event_type: typing_extensions.Annotated[
        TelemetryEventEventType, FieldMetadata(alias="eventType"), pydantic.Field(alias="eventType")
    ]
    page: str
    action: str
    correlation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="correlationId"), pydantic.Field(alias="correlationId")
    ] = None
    metadata: typing.Optional[typing.Dict[str, str]] = None
    timestamp: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
