

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_part_input_source import AgentPartInputSource
from .file_part_source import FilePartSource
from .subtask_part_input_model import SubtaskPartInputModel
from .text_part_input_time import TextPartInputTime


class SessionPromptRequestPartsItem_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    id: typing.Optional[str] = None
    text: str
    synthetic: typing.Optional[bool] = None
    ignored: typing.Optional[bool] = None
    time: typing.Optional[TextPartInputTime] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionPromptRequestPartsItem_File(UniversalBaseModel):
    type: typing.Literal["file"] = "file"
    id: typing.Optional[str] = None
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


class SessionPromptRequestPartsItem_Agent(UniversalBaseModel):
    type: typing.Literal["agent"] = "agent"
    id: typing.Optional[str] = None
    name: str
    source: typing.Optional[AgentPartInputSource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SessionPromptRequestPartsItem_Subtask(UniversalBaseModel):
    type: typing.Literal["subtask"] = "subtask"
    id: typing.Optional[str] = None
    prompt: str
    description: str
    agent: str
    model: typing.Optional[SubtaskPartInputModel] = None
    command: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SessionPromptRequestPartsItem = typing_extensions.Annotated[
    typing.Union[
        SessionPromptRequestPartsItem_Text,
        SessionPromptRequestPartsItem_File,
        SessionPromptRequestPartsItem_Agent,
        SessionPromptRequestPartsItem_Subtask,
    ],
    pydantic.Field(discriminator="type"),
]
