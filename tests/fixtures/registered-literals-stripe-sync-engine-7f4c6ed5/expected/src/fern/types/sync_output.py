

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .connection_status_message_connection_status import ConnectionStatusMessageConnectionStatus
from .control_message_control import ControlMessageControl
from .eof_payload import EofPayload
from .log_message_log import LogMessageLog
from .progress_payload import ProgressPayload
from .source_state_message_source_state import SourceStateMessageSourceState
from .stream_status_message_stream_status import StreamStatusMessageStreamStatus


class SyncOutput_SourceState(UniversalBaseModel):
    type: typing.Literal["source_state"] = "source_state"
    emitted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_emitted_by"), pydantic.Field(alias="_emitted_by")
    ] = None
    ts: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="_ts"), pydantic.Field(alias="_ts")
    ] = None
    source_state: SourceStateMessageSourceState

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SyncOutput_StreamStatus(UniversalBaseModel):
    type: typing.Literal["stream_status"] = "stream_status"
    emitted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_emitted_by"), pydantic.Field(alias="_emitted_by")
    ] = None
    ts: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="_ts"), pydantic.Field(alias="_ts")
    ] = None
    stream_status: StreamStatusMessageStreamStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SyncOutput_Progress(UniversalBaseModel):
    type: typing.Literal["progress"] = "progress"
    emitted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_emitted_by"), pydantic.Field(alias="_emitted_by")
    ] = None
    ts: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="_ts"), pydantic.Field(alias="_ts")
    ] = None
    progress: ProgressPayload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SyncOutput_ConnectionStatus(UniversalBaseModel):
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


class SyncOutput_Log(UniversalBaseModel):
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


class SyncOutput_Eof(UniversalBaseModel):
    type: typing.Literal["eof"] = "eof"
    emitted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_emitted_by"), pydantic.Field(alias="_emitted_by")
    ] = None
    ts: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="_ts"), pydantic.Field(alias="_ts")
    ] = None
    eof: EofPayload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SyncOutput_Control(UniversalBaseModel):
    type: typing.Literal["control"] = "control"
    emitted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_emitted_by"), pydantic.Field(alias="_emitted_by")
    ] = None
    ts: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="_ts"), pydantic.Field(alias="_ts")
    ] = None
    control: ControlMessageControl

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SyncOutput = typing_extensions.Annotated[
    typing.Union[
        SyncOutput_SourceState,
        SyncOutput_StreamStatus,
        SyncOutput_Progress,
        SyncOutput_ConnectionStatus,
        SyncOutput_Log,
        SyncOutput_Eof,
        SyncOutput_Control,
    ],
    pydantic.Field(discriminator="type"),
]
