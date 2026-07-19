

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.update_assistant_message_content import UpdateAssistantMessageContent
from ...types.update_user_message_content import UpdateUserMessageContent


class ModifyGroupMessageRequestBody_SystemMessage(UniversalBaseModel):
    message_type: typing.Literal["system_message"] = "system_message"
    content: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModifyGroupMessageRequestBody_UserMessage(UniversalBaseModel):
    message_type: typing.Literal["user_message"] = "user_message"
    content: UpdateUserMessageContent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModifyGroupMessageRequestBody_ReasoningMessage(UniversalBaseModel):
    message_type: typing.Literal["reasoning_message"] = "reasoning_message"
    reasoning: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModifyGroupMessageRequestBody_AssistantMessage(UniversalBaseModel):
    message_type: typing.Literal["assistant_message"] = "assistant_message"
    content: UpdateAssistantMessageContent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ModifyGroupMessageRequestBody = typing_extensions.Annotated[
    typing.Union[
        ModifyGroupMessageRequestBody_SystemMessage,
        ModifyGroupMessageRequestBody_UserMessage,
        ModifyGroupMessageRequestBody_ReasoningMessage,
        ModifyGroupMessageRequestBody_AssistantMessage,
    ],
    pydantic.Field(discriminator="message_type"),
]
