

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class BillingLimitResponse(UniversalBaseModel):
    max_website_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="maxWebsiteCount"), pydantic.Field(alias="maxWebsiteCount")
    ]
    max_website_event_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="maxWebsiteEventCount"), pydantic.Field(alias="maxWebsiteEventCount")
    ]
    max_monitor_execution_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="maxMonitorExecutionCount"), pydantic.Field(alias="maxMonitorExecutionCount")
    ]
    max_survey_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="maxSurveyCount"), pydantic.Field(alias="maxSurveyCount")
    ]
    max_feed_channel_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="maxFeedChannelCount"), pydantic.Field(alias="maxFeedChannelCount")
    ]
    max_feed_event_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="maxFeedEventCount"), pydantic.Field(alias="maxFeedEventCount")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
