

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_sources_post_error413error import PromptsSourcesPostError413Error
from .prompts_sources_post_error413meta import PromptsSourcesPostError413Meta


class PromptsSourcesPostError413(UniversalBaseModel):
    success: bool
    error: PromptsSourcesPostError413Error
    meta: typing.Optional[PromptsSourcesPostError413Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
