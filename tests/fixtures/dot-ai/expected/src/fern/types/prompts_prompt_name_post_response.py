

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_prompt_name_post_response_data import PromptsPromptNamePostResponseData
from .prompts_prompt_name_post_response_meta import PromptsPromptNamePostResponseMeta


class PromptsPromptNamePostResponse(UniversalBaseModel):
    success: bool
    data: PromptsPromptNamePostResponseData
    meta: typing.Optional[PromptsPromptNamePostResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
