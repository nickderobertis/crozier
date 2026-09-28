

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_prompt_name_post_error502error import PromptsPromptNamePostError502Error
from .prompts_prompt_name_post_error502meta import PromptsPromptNamePostError502Meta


class PromptsPromptNamePostError502(UniversalBaseModel):
    success: bool
    error: PromptsPromptNamePostError502Error
    meta: typing.Optional[PromptsPromptNamePostError502Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
