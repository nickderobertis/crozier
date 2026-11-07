

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_ocs_get_capabilities200response_ocs_data_capabilities_provisioning_api import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesProvisioningApi,
)


class ProvisioningApiCapabilities(UniversalBaseModel):
    provisioning_api: CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesProvisioningApi

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
