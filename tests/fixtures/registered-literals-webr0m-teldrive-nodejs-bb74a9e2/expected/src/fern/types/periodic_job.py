

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PeriodicJob(UniversalBaseModel):
    id: str
    kind: str
    args: typing.Dict[str, typing.Any]
    queue: str
    priority: int
    max_attempts: typing_extensions.Annotated[
        int, FieldMetadata(alias="maxAttempts"), pydantic.Field(alias="maxAttempts")
    ]
    tags: typing.List[str]
    cron_expression: typing_extensions.Annotated[
        str, FieldMetadata(alias="cronExpression"), pydantic.Field(alias="cronExpression")
    ]
    cron_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="cronTimezone"), pydantic.Field(alias="cronTimezone")
    ]
    next_run_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="nextRunAt"), pydantic.Field(alias="nextRunAt")
    ]
    paused: bool
    paused_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="pausedAt"), pydantic.Field(alias="pausedAt")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
