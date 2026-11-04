

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_reference_api_resolve_one200response_ocs_data import CoreReferenceApiResolveOne200ResponseOcsData
from .ocs_meta import OcsMeta


class CoreReferenceApiResolveOne200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: CoreReferenceApiResolveOne200ResponseOcsData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
