

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ApplicationEventStatsResponsePreviousItem(UniversalBaseModel):
    date: str
    event_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="eventCount"), pydantic.Field(alias="eventCount")
    ]
    session_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="sessionCount"), pydantic.Field(alias="sessionCount")
    ]
    total_time: typing_extensions.Annotated[float, FieldMetadata(alias="totalTime"), pydantic.Field(alias="totalTime")]
    avg_events_per_session: typing_extensions.Annotated[
        float, FieldMetadata(alias="avgEventsPerSession"), pydantic.Field(alias="avgEventsPerSession")
    ]
    avg_screens_per_session: typing_extensions.Annotated[
        float, FieldMetadata(alias="avgScreensPerSession"), pydantic.Field(alias="avgScreensPerSession")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
