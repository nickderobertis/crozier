

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .prompt_one_type import PromptOneType
from .text_prompt import TextPrompt


class PromptOne(TextPrompt):
    type: PromptOneType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
