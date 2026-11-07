

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .daily_usage_response_api_calls_billable import DailyUsageResponseApiCallsBillable
from .daily_usage_response_api_calls_credited import DailyUsageResponseApiCallsCredited
from .daily_usage_response_api_calls_made import DailyUsageResponseApiCallsMade


class DailyUsageResponse(UniversalBaseModel):
    api_calls_billable: typing_extensions.Annotated[
        DailyUsageResponseApiCallsBillable,
        FieldMetadata(alias="apiCallsBillable"),
        pydantic.Field(alias="apiCallsBillable", description="Total number of API calls billed for the billing cycle."),
    ]
    """
    Total number of API calls billed for the billing cycle.
    """

    api_calls_credited: typing_extensions.Annotated[
        DailyUsageResponseApiCallsCredited,
        FieldMetadata(alias="apiCallsCredited"),
        pydantic.Field(
            alias="apiCallsCredited",
            description="Total number of callbackFailures including caseUpdate, caseDocumentOrder and caseExport for the billing cycle.",
        ),
    ]
    """
    Total number of callbackFailures including caseUpdate, caseDocumentOrder and caseExport for the billing cycle.
    """

    api_calls_made: typing_extensions.Annotated[
        DailyUsageResponseApiCallsMade,
        FieldMetadata(alias="apiCallsMade"),
        pydantic.Field(alias="apiCallsMade", description="Total API calls made for the billing cycle."),
    ]
    """
    Total API calls made for the billing cycle.
    """

    api_usage: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="apiUsage"),
        pydantic.Field(alias="apiUsage", description="Api Usage made."),
    ]
    """
    Api Usage made.
    """

    object: str = pydantic.Field()
    """
    Name of the object.
    """

    usage_end_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="usageEndTime"),
        pydantic.Field(alias="usageEndTime", description="End time of the usage."),
    ]
    """
    End time of the usage.
    """

    usage_start_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="usageStartTime"),
        pydantic.Field(alias="usageStartTime", description="Start time of the usage."),
    ]
    """
    Start time of the usage.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
