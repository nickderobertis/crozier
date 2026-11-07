

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provisioning_api_apps_get_apps200response_ocs import ProvisioningApiAppsGetApps200ResponseOcs


class ProvisioningApiAppsGetApps200Response(UniversalBaseModel):
    ocs: ProvisioningApiAppsGetApps200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
