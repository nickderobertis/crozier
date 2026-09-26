

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_part import FilePart
from .tool_state_completed_time import ToolStateCompletedTime
from .tool_state_error_time import ToolStateErrorTime
from .tool_state_running_time import ToolStateRunningTime


class ToolState_Pending(UniversalBaseModel):
    status: typing.Literal["pending"] = "pending"
    input: typing.Dict[str, typing.Any]
    raw: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ToolState_Running(UniversalBaseModel):
    status: typing.Literal["running"] = "running"
    input: typing.Dict[str, typing.Any]
    title: typing.Optional[str] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    time: ToolStateRunningTime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ToolState_Completed(UniversalBaseModel):
    status: typing.Literal["completed"] = "completed"
    input: typing.Dict[str, typing.Any]
    output: str
    title: str
    metadata: typing.Dict[str, typing.Any]
    time: ToolStateCompletedTime
    attachments: typing.Optional[typing.List[FilePart]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ToolState_Error(UniversalBaseModel):
    status: typing.Literal["error"] = "error"
    input: typing.Dict[str, typing.Any]
    error: str
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    time: ToolStateErrorTime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ToolState = typing_extensions.Annotated[
    typing.Union[ToolState_Pending, ToolState_Running, ToolState_Completed, ToolState_Error],
    pydantic.Field(discriminator="status"),
]
