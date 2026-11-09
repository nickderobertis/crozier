

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .create_prompt_request_one_type import CreatePromptRequestOneType
from .create_text_prompt_request import CreateTextPromptRequest


class CreatePromptRequestOne(CreateTextPromptRequest):
    type: CreatePromptRequestOneType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
