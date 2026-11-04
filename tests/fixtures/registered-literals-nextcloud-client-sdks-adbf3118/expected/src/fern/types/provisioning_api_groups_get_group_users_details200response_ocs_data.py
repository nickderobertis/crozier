

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provisioning_api_groups_get_group_users_details200response_ocs_data_users_value import (
    ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsDataUsersValue,
)


class ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsData(UniversalBaseModel):
    users: typing.Dict[str, ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsDataUsersValue]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
