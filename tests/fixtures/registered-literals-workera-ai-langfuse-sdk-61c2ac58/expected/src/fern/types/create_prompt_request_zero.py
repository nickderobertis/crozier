

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .create_chat_prompt_request import CreateChatPromptRequest
from .create_prompt_request_zero_type import CreatePromptRequestZeroType


class CreatePromptRequestZero(CreateChatPromptRequest):
    type: CreatePromptRequestZeroType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
