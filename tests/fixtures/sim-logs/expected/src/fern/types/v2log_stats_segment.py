

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2LogStatsSegment(UniversalBaseModel):
    """
    Run counts and mean latency for one time bucket.
    """

    timestamp: dt.datetime = pydantic.Field()
    """
    ISO 8601 start of the bucket.
    """

    total_executions: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="totalExecutions"),
        pydantic.Field(alias="totalExecutions", description="Runs that started inside the bucket."),
    ]
    """
    Runs that started inside the bucket.
    """

    successful_executions: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="successfulExecutions"),
        pydantic.Field(alias="successfulExecutions", description="Runs in the bucket that did not error."),
    ]
    """
    Runs in the bucket that did not error.
    """

    avg_duration_ms: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="avgDurationMs"),
        pydantic.Field(
            alias="avgDurationMs",
            description="Mean duration of the bucket's runs in milliseconds, weighted by run count. Zero when no run in the bucket recorded a duration.",
        ),
    ]
    """
    Mean duration of the bucket's runs in milliseconds, weighted by run count. Zero when no run in the bucket recorded a duration.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
