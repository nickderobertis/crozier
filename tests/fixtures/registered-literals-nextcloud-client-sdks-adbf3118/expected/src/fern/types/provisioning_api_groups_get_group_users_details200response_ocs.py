

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocs_meta import OcsMeta
from .provisioning_api_groups_get_group_users_details200response_ocs_data import (
    ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsData,
)


class ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: ProvisioningApiGroupsGetGroupUsersDetails200ResponseOcsData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
