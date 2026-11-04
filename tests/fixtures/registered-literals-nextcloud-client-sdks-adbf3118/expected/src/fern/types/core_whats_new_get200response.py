

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_whats_new_get200response_ocs import CoreWhatsNewGet200ResponseOcs


class CoreWhatsNewGet200Response(UniversalBaseModel):
    ocs: CoreWhatsNewGet200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
