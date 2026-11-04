

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provisioning_api_users_add_user200response_ocs import ProvisioningApiUsersAddUser200ResponseOcs


class ProvisioningApiUsersAddUser200Response(UniversalBaseModel):
    ocs: ProvisioningApiUsersAddUser200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
