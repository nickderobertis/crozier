

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_get_error502error import PromptsGetError502Error
from .prompts_get_error502meta import PromptsGetError502Meta


class PromptsGetError502(UniversalBaseModel):
    success: bool
    error: PromptsGetError502Error
    meta: typing.Optional[PromptsGetError502Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
