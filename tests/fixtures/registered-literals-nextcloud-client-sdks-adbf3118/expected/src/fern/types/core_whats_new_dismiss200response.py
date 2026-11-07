

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_whats_new_dismiss200response_ocs import CoreWhatsNewDismiss200ResponseOcs


class CoreWhatsNewDismiss200Response(UniversalBaseModel):
    ocs: CoreWhatsNewDismiss200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
