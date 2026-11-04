

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provisioning_api_users_search_by_phone_numbers200response_ocs import (
    ProvisioningApiUsersSearchByPhoneNumbers200ResponseOcs,
)


class ProvisioningApiUsersSearchByPhoneNumbers200Response(UniversalBaseModel):
    ocs: ProvisioningApiUsersSearchByPhoneNumbers200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
