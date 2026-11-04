

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_reference_api_touch_provider200response_ocs import CoreReferenceApiTouchProvider200ResponseOcs


class CoreReferenceApiTouchProvider200Response(UniversalBaseModel):
    ocs: CoreReferenceApiTouchProvider200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
