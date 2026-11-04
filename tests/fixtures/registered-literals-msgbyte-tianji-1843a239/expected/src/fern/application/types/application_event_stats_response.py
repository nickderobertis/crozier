

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .application_event_stats_response_current_item import ApplicationEventStatsResponseCurrentItem
from .application_event_stats_response_previous_item import ApplicationEventStatsResponsePreviousItem


class ApplicationEventStatsResponse(UniversalBaseModel):
    current: typing.List[ApplicationEventStatsResponseCurrentItem]
    previous: typing.List[ApplicationEventStatsResponsePreviousItem]
    current_total_session_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="currentTotalSessionCount"), pydantic.Field(alias="currentTotalSessionCount")
    ]
    previous_total_session_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="previousTotalSessionCount"), pydantic.Field(alias="previousTotalSessionCount")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
