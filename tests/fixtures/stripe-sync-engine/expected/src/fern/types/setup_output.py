

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .control_message_control import ControlMessageControl
from .log_message_log import LogMessageLog


class SetupOutput_Control(UniversalBaseModel):
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


class SetupOutput_Log(UniversalBaseModel):
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


SetupOutput = typing_extensions.Annotated[
    typing.Union[SetupOutput_Control, SetupOutput_Log], pydantic.Field(discriminator="type")
]
