

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .audit_event_dto import AuditEventDto
from .json_node import JsonNode


class SystemAuditEventDto(AuditEventDto):
    error_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="errorTime"),
        pydantic.Field(alias="errorTime", description="Time when an error occurred, if applicable"),
    ] = None
    """
    Time when an error occurred, if applicable
    """

    done_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="doneTime"),
        pydantic.Field(alias="doneTime", description="Time when the operation completed, if applicable"),
    ] = None
    """
    Time when the operation completed, if applicable
    """

    queue_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="queueName"),
        pydantic.Field(alias="queueName", description="Name of the queue involved in the operation, if applicable"),
    ] = None
    """
    Name of the queue involved in the operation, if applicable
    """

    shard_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shardId"),
        pydantic.Field(alias="shardId", description="Identifier of the shard involved in the operation, if applicable"),
    ] = None
    """
    Identifier of the shard involved in the operation, if applicable
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Status of the system operation, if applicable
    """

    data: typing.Optional[JsonNode] = pydantic.Field(default=None)
    """
    Object containing specific event data with technical information
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
