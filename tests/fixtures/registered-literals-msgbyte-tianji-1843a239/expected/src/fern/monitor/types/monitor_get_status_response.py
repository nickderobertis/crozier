

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .monitor_get_status_response_payload import MonitorGetStatusResponsePayload


class MonitorGetStatusResponse(UniversalBaseModel):
    monitor_id: typing_extensions.Annotated[str, FieldMetadata(alias="monitorId"), pydantic.Field(alias="monitorId")]
    status_name: typing_extensions.Annotated[str, FieldMetadata(alias="statusName"), pydantic.Field(alias="statusName")]
    payload: typing.Optional[MonitorGetStatusResponsePayload] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
