

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class BillingUsageResponse(UniversalBaseModel):
    website_accepted_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="websiteAcceptedCount"), pydantic.Field(alias="websiteAcceptedCount")
    ]
    website_event_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="websiteEventCount"), pydantic.Field(alias="websiteEventCount")
    ]
    monitor_execution_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="monitorExecutionCount"), pydantic.Field(alias="monitorExecutionCount")
    ]
    survey_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="surveyCount"), pydantic.Field(alias="surveyCount")
    ]
    feed_event_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="feedEventCount"), pydantic.Field(alias="feedEventCount")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
