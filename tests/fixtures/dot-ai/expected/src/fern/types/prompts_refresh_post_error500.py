

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_refresh_post_error500error import PromptsRefreshPostError500Error
from .prompts_refresh_post_error500meta import PromptsRefreshPostError500Meta


class PromptsRefreshPostError500(UniversalBaseModel):
    success: bool
    error: PromptsRefreshPostError500Error
    meta: typing.Optional[PromptsRefreshPostError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
