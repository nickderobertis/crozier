

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ConnectionScheduleDataCron(UniversalBaseModel):
    cron_expression: typing_extensions.Annotated[
        str, FieldMetadata(alias="cronExpression"), pydantic.Field(alias="cronExpression")
    ]
    cron_time_zone: typing_extensions.Annotated[
        str, FieldMetadata(alias="cronTimeZone"), pydantic.Field(alias="cronTimeZone")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
