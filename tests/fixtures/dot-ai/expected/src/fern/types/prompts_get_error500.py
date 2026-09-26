

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .prompts_get_error500error import PromptsGetError500Error
from .prompts_get_error500meta import PromptsGetError500Meta


class PromptsGetError500(UniversalBaseModel):
    success: bool
    error: PromptsGetError500Error
    meta: typing.Optional[PromptsGetError500Meta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
