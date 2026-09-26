

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .internal_dispatch_schedules_response_status import InternalDispatchSchedulesResponseStatus


class InternalDispatchSchedulesResponse(UniversalBaseModel):
    status: InternalDispatchSchedulesResponseStatus
    cutoff_minute: typing_extensions.Annotated[
        str, FieldMetadata(alias="cutoffMinute"), pydantic.Field(alias="cutoffMinute")
    ]
    idempotency_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="idempotencyKey"), pydantic.Field(alias="idempotencyKey")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
