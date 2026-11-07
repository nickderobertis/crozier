

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_ocs_get_capabilities200response_ocs_data_capabilities import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilities,
)
from .core_ocs_get_capabilities200response_ocs_data_version import CoreOcsGetCapabilities200ResponseOcsDataVersion


class CoreOcsGetCapabilities200ResponseOcsData(UniversalBaseModel):
    version: CoreOcsGetCapabilities200ResponseOcsDataVersion
    capabilities: CoreOcsGetCapabilities200ResponseOcsDataCapabilities

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
