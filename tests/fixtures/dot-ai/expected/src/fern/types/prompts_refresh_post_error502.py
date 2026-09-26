

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_refresh_post_error502error import PromptsRefreshPostError502Error
from .prompts_refresh_post_error502meta import PromptsRefreshPostError502Meta


class PromptsRefreshPostError502(UniversalBaseModel):
    success: bool
    error: PromptsRefreshPostError502Error
    meta: typing.Optional[PromptsRefreshPostError502Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
