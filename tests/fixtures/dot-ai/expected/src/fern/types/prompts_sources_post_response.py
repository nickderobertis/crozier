

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_sources_post_response_data import PromptsSourcesPostResponseData
from .prompts_sources_post_response_meta import PromptsSourcesPostResponseMeta


class PromptsSourcesPostResponse(UniversalBaseModel):
    success: bool
    data: PromptsSourcesPostResponseData
    meta: typing.Optional[PromptsSourcesPostResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
