

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .catalog_message_catalog import CatalogMessageCatalog
from .connection_status_message_connection_status import ConnectionStatusMessageConnectionStatus
from .control_message_control import ControlMessageControl
from .eof_payload import EofPayload
from .log_message_log import LogMessageLog
from .progress_payload import ProgressPayload
from .record_message_record import RecordMessageRecord
from .source_state_message_source_state import SourceStateMessageSourceState
from .spec_message_spec import SpecMessageSpec
from .stream_status_message_stream_status import StreamStatusMessageStreamStatus


class Message_Record(UniversalBaseModel):
    type: typing.Literal["record"] = "record"
    emitted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_emitted_by"), pydantic.Field(alias="_emitted_by")
    ] = None
    ts: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="_ts"), pydantic.Field(alias="_ts")
    ] = None
    record: RecordMessageRecord

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Message_SourceState(UniversalBaseModel):
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


class Message_Catalog(UniversalBaseModel):
    type: typing.Literal["catalog"] = "catalog"
    emitted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_emitted_by"), pydantic.Field(alias="_emitted_by")
    ] = None
    ts: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="_ts"), pydantic.Field(alias="_ts")
    ] = None
    catalog: CatalogMessageCatalog

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Message_Log(UniversalBaseModel):
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


class Message_Spec(UniversalBaseModel):
    type: typing.Literal["spec"] = "spec"
    emitted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_emitted_by"), pydantic.Field(alias="_emitted_by")
    ] = None
    ts: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="_ts"), pydantic.Field(alias="_ts")
    ] = None
    spec: SpecMessageSpec

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Message_ConnectionStatus(UniversalBaseModel):
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


class Message_StreamStatus(UniversalBaseModel):
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


class Message_Control(UniversalBaseModel):
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


class Message_Progress(UniversalBaseModel):
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


class Message_Eof(UniversalBaseModel):
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


class Message_SourceInput(UniversalBaseModel):
    type: typing.Literal["source_input"] = "source_input"
    emitted_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="_emitted_by"), pydantic.Field(alias="_emitted_by")
    ] = None
    ts: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="_ts"), pydantic.Field(alias="_ts")
    ] = None
    source_input: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Message = typing_extensions.Annotated[
    typing.Union[
        Message_Record,
        Message_SourceState,
        Message_Catalog,
        Message_Log,
        Message_Spec,
        Message_ConnectionStatus,
        Message_StreamStatus,
        Message_Control,
        Message_Progress,
        Message_Eof,
        Message_SourceInput,
    ],
    pydantic.Field(discriminator="type"),
]
