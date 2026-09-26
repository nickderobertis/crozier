

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .assistant_message_error import AssistantMessageError
from .assistant_message_path import AssistantMessagePath
from .assistant_message_time import AssistantMessageTime
from .assistant_message_tokens import AssistantMessageTokens
from .user_message_model import UserMessageModel
from .user_message_summary import UserMessageSummary
from .user_message_time import UserMessageTime


class Message_User(UniversalBaseModel):
    role: typing.Literal["user"] = "user"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    time: UserMessageTime
    summary: typing.Optional[UserMessageSummary] = None
    agent: str
    model: UserMessageModel
    system: typing.Optional[str] = None
    tools: typing.Optional[typing.Dict[str, bool]] = None
    variant: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Message_Assistant(UniversalBaseModel):
    role: typing.Literal["assistant"] = "assistant"
    id: str
    session_id: typing_extensions.Annotated[str, FieldMetadata(alias="sessionID"), pydantic.Field(alias="sessionID")]
    time: AssistantMessageTime
    error: typing.Optional[AssistantMessageError] = None
    parent_id: typing_extensions.Annotated[str, FieldMetadata(alias="parentID"), pydantic.Field(alias="parentID")]
    model_id: typing_extensions.Annotated[str, FieldMetadata(alias="modelID"), pydantic.Field(alias="modelID")]
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerID"), pydantic.Field(alias="providerID")]
    mode: str
    agent: str
    path: AssistantMessagePath
    summary: typing.Optional[bool] = None
    cost: float
    tokens: AssistantMessageTokens
    finish: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Message = typing_extensions.Annotated[
    typing.Union[Message_User, Message_Assistant], pydantic.Field(discriminator="role")
]
