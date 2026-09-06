

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_message_param import ChatCompletionMessageParam


class PromptBlockData_Chat(UniversalBaseModel):
    type: typing.Literal["chat"] = "chat"
    messages: typing.List[ChatCompletionMessageParam]
    tools: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PromptBlockData_Completion(UniversalBaseModel):
    type: typing.Literal["completion"] = "completion"
    content: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PromptBlockData = typing_extensions.Annotated[
    typing.Union[PromptBlockData_Chat, PromptBlockData_Completion], pydantic.Field(discriminator="type")
]
