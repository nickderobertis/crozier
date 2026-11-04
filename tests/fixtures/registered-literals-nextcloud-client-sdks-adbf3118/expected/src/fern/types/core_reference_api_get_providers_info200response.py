

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_reference_api_get_providers_info200response_ocs import CoreReferenceApiGetProvidersInfo200ResponseOcs


class CoreReferenceApiGetProvidersInfo200Response(UniversalBaseModel):
    ocs: CoreReferenceApiGetProvidersInfo200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
