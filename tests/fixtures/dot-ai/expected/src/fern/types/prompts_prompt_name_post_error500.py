

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_prompt_name_post_error500error import PromptsPromptNamePostError500Error
from .prompts_prompt_name_post_error500meta import PromptsPromptNamePostError500Meta


class PromptsPromptNamePostError500(UniversalBaseModel):
    success: bool
    error: PromptsPromptNamePostError500Error
    meta: typing.Optional[PromptsPromptNamePostError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
