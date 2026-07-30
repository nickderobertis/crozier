

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .connection_status_message_connection_status import ConnectionStatusMessageConnectionStatus
from .log_message_log import LogMessageLog


class CheckOutput_ConnectionStatus(UniversalBaseModel):
    type: typing.Literal["connection_status"] = "connection_status"
    emitted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_emitted_by"), pydantic.Field(alias="_emitted_by")
    ] = None
    ts: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="_ts"), pydantic.Field(alias="_ts")
    ] = None
    connection_status: ConnectionStatusMessageConnectionStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CheckOutput_Log(UniversalBaseModel):
    type: typing.Literal["log"] = "log"
    emitted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_emitted_by"), pydantic.Field(alias="_emitted_by")
    ] = None
    ts: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="_ts"), pydantic.Field(alias="_ts")
    ] = None
    log: LogMessageLog

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CheckOutput = typing_extensions.Annotated[
    typing.Union[CheckOutput_ConnectionStatus, CheckOutput_Log], pydantic.Field(discriminator="type")
]
