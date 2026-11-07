

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocs_meta import OcsMeta
from .provisioning_api_app_config_get_value200response_ocs_data import (
    ProvisioningApiAppConfigGetValue200ResponseOcsData,
)


class ProvisioningApiAppConfigGetValue200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: ProvisioningApiAppConfigGetValue200ResponseOcsData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
