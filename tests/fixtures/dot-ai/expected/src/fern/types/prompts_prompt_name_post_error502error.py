

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_prompt_name_post_error502error_code import PromptsPromptNamePostError502ErrorCode


class PromptsPromptNamePostError502Error(UniversalBaseModel):
    code: PromptsPromptNamePostError502ErrorCode
    message: str
    details: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
