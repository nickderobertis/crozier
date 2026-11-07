

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provisioning_api_app_config_get_value200response_ocs import ProvisioningApiAppConfigGetValue200ResponseOcs


class ProvisioningApiAppConfigGetValue200Response(UniversalBaseModel):
    ocs: ProvisioningApiAppConfigGetValue200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
