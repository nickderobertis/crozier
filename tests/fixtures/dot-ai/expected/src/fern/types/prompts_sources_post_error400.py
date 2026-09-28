

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_sources_post_error400error import PromptsSourcesPostError400Error
from .prompts_sources_post_error400meta import PromptsSourcesPostError400Meta


class PromptsSourcesPostError400(UniversalBaseModel):
    success: bool
    error: PromptsSourcesPostError400Error
    meta: typing.Optional[PromptsSourcesPostError400Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
