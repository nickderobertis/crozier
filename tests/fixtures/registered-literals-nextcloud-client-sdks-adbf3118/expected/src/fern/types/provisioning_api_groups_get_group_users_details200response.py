

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provisioning_api_groups_get_group_users_details200response_ocs import (
    ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcs,
)


class ProvisioningApiGroupsGetGroupUsersDetails200Response(UniversalBaseModel):
    ocs: ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
