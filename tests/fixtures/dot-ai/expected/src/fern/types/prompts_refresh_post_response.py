

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_refresh_post_response_data import PromptsRefreshPostResponseData
from .prompts_refresh_post_response_meta import PromptsRefreshPostResponseMeta


class PromptsRefreshPostResponse(UniversalBaseModel):
    success: bool
    data: PromptsRefreshPostResponseData
    meta: typing.Optional[PromptsRefreshPostResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
