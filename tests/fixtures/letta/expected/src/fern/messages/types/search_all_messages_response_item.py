

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.assistant_message_list_result_content import AssistantMessageListResultContent
from ...types.user_message_list_result_content import UserMessageListResultContent


class SearchAllMessagesResponseItem_SystemMessage(UniversalBaseModel):
    message_type: typing.Literal["system_message"] = "system_message"
    content: str
    message_id: str
    agent_id: typing.Optional[str] = None
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchAllMessagesResponseItem_UserMessage(UniversalBaseModel):
    message_type: typing.Literal["user_message"] = "user_message"
    content: UserMessageListResultContent
    message_id: str
    agent_id: typing.Optional[str] = None
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchAllMessagesResponseItem_ReasoningMessage(UniversalBaseModel):
    message_type: typing.Literal["reasoning_message"] = "reasoning_message"
    reasoning: str
    message_id: str
    agent_id: typing.Optional[str] = None
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SearchAllMessagesResponseItem_AssistantMessage(UniversalBaseModel):
    message_type: typing.Literal["assistant_message"] = "assistant_message"
    content: AssistantMessageListResultContent
    message_id: str
    agent_id: typing.Optional[str] = None
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SearchAllMessagesResponseItem = typing_extensions.Annotated[
    typing.Union[
        SearchAllMessagesResponseItem_SystemMessage,
        SearchAllMessagesResponseItem_UserMessage,
        SearchAllMessagesResponseItem_ReasoningMessage,
        SearchAllMessagesResponseItem_AssistantMessage,
    ],
    pydantic.Field(discriminator="message_type"),
]
