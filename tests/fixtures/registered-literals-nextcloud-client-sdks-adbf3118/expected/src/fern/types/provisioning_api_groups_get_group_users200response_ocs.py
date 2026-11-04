

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocs_meta import OcsMeta
from .provisioning_api_groups_get_group_users200response_ocs_data import (
    ProvisioningApiGroupsGetGroupUsers200ResponseOcsData,
)


class ProvisioningApiGroupsGetGroupUsers200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: ProvisioningApiGroupsGetGroupUsers200ResponseOcsData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
