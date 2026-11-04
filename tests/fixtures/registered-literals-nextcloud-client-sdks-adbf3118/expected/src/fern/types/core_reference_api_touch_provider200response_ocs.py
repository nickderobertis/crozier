

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_reference_api_touch_provider200response_ocs_data import CoreReferenceApiTouchProvider200ResponseOcsData
from .ocs_meta import OcsMeta


class CoreReferenceApiTouchProvider200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: CoreReferenceApiTouchProvider200ResponseOcsData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
