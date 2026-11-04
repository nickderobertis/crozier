

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_unified_search_provider import CoreUnifiedSearchProvider
from .ocs_meta import OcsMeta


class CoreUnifiedSearchGetProviders200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: typing.List[CoreUnifiedSearchProvider]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
