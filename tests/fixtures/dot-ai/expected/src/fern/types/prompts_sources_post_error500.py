

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_sources_post_error500error import PromptsSourcesPostError500Error
from .prompts_sources_post_error500meta import PromptsSourcesPostError500Meta


class PromptsSourcesPostError500(UniversalBaseModel):
    success: bool
    error: PromptsSourcesPostError500Error
    meta: typing.Optional[PromptsSourcesPostError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
