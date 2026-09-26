

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_prompt_name_post_error404error import PromptsPromptNamePostError404Error
from .prompts_prompt_name_post_error404meta import PromptsPromptNamePostError404Meta


class PromptsPromptNamePostError404(UniversalBaseModel):
    success: bool
    error: PromptsPromptNamePostError404Error
    meta: typing.Optional[PromptsPromptNamePostError404Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
