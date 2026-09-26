

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_prompt_name_post_error400error import PromptsPromptNamePostError400Error
from .prompts_prompt_name_post_error400meta import PromptsPromptNamePostError400Meta


class PromptsPromptNamePostError400(UniversalBaseModel):
    success: bool
    error: PromptsPromptNamePostError400Error
    meta: typing.Optional[PromptsPromptNamePostError400Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
