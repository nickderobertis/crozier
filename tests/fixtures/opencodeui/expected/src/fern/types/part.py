

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .agent_part_source import AgentPartSource
from .api_error import ApiError
from .file_part_source import FilePartSource
from .reasoning_part_time import ReasoningPartTime
from .retry_part_time import RetryPartTime
from .step_finish_part_tokens import StepFinishPartTokens
from .subtask_part_model import SubtaskPartModel
from .text_part_time import TextPartTime
from .tool_state import ToolState


class Part_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    text: str
    synthetic: typing.Optional[bool] = None
    ignored: typing.Optional[bool] = None
    time: typing.Optional[TextPartTime] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Part_Subtask(UniversalBaseModel):
    type: typing.Literal["subtask"] = "subtask"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    prompt: str
    description: str
    agent: str
    model: typing.Optional[SubtaskPartModel] = None
    command: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Part_Reasoning(UniversalBaseModel):
    type: typing.Literal["reasoning"] = "reasoning"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    text: str
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    time: ReasoningPartTime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Part_File(UniversalBaseModel):
    type: typing.Literal["file"] = "file"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    mime: str
    filename: typing.Optional[str] = None
    url: str
    source: typing.Optional[FilePartSource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Part_Tool(UniversalBaseModel):
    type: typing.Literal["tool"] = "tool"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    call_id: typing_extensions.Annotated[str, FieldMetadata(alias="callID"), pydantic.Field(alias="callID")]
    tool: str
    state: ToolState
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Part_StepStart(UniversalBaseModel):
    type: typing.Literal["step-start"] = "step-start"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    snapshot: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Part_StepFinish(UniversalBaseModel):
    type: typing.Literal["step-finish"] = "step-finish"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    reason: str
    snapshot: typing.Optional[str] = None
    cost: float
    tokens: StepFinishPartTokens

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Part_Snapshot(UniversalBaseModel):
    type: typing.Literal["snapshot"] = "snapshot"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    snapshot: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Part_Patch(UniversalBaseModel):
    type: typing.Literal["patch"] = "patch"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    hash: str
    files: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Part_Agent(UniversalBaseModel):
    type: typing.Literal["agent"] = "agent"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    name: str
    source: typing.Optional[AgentPartSource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Part_Retry(UniversalBaseModel):
    type: typing.Literal["retry"] = "retry"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    attempt: float
    error: ApiError
    time: RetryPartTime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Part_Compaction(UniversalBaseModel):
    type: typing.Literal["compaction"] = "compaction"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    message_id: typing_extensions.Annotated[str, FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")]
    auto: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Part = typing_extensions.Annotated[
    typing.Union[
        Part_Text,
        Part_Subtask,
        Part_Reasoning,
        Part_File,
        Part_Tool,
        Part_StepStart,
        Part_StepFinish,
        Part_Snapshot,
        Part_Patch,
        Part_Agent,
        Part_Retry,
        Part_Compaction,
    ],
    pydantic.Field(discriminator="type"),
]
