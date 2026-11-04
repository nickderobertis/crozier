

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_unified_search_get_providers200response_ocs import CoreUnifiedSearchGetProviders200ResponseOcs


class CoreUnifiedSearchGetProviders200Response(UniversalBaseModel):
    ocs: CoreUnifiedSearchGetProviders200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
