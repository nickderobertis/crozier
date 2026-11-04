

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocs_meta import OcsMeta
from .provisioning_api_groups_get_group_users_details200response_ocs_data_users_value_one_of import (
    ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsDataUsersValueOneOf,
)


class ProvisioningApiUsersAddUser200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsDataUsersValueOneOf

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
