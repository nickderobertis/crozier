

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provisioning_api_groups_get_sub_admins_of_group200response_ocs import (
    ProvisioningApiGroupsGetSubAdminsOfGroup200ResponseOcs,
)


class ProvisioningApiGroupsGetSubAdminsOfGroup200Response(UniversalBaseModel):
    ocs: ProvisioningApiGroupsGetSubAdminsOfGroup200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
