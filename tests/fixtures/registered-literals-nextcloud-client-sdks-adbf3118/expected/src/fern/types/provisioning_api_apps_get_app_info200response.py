

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provisioning_api_apps_get_app_info200response_ocs import ProvisioningApiAppsGetAppInfo200ResponseOcs


class ProvisioningApiAppsGetAppInfo200Response(UniversalBaseModel):
    ocs: ProvisioningApiAppsGetAppInfo200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
