

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_get_error400error import PromptsGetError400Error
from .prompts_get_error400meta import PromptsGetError400Meta


class PromptsGetError400(UniversalBaseModel):
    success: bool
    error: PromptsGetError400Error
    meta: typing.Optional[PromptsGetError400Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
