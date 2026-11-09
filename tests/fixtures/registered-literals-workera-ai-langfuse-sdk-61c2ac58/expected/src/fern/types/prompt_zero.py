

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .chat_prompt import ChatPrompt
from .prompt_zero_type import PromptZeroType


class PromptZero(ChatPrompt):
    type: PromptZeroType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
