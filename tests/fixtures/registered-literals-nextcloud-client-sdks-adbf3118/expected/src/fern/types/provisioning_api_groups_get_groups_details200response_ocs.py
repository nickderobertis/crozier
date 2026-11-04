

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocs_meta import OcsMeta
from .provisioning_api_groups_get_groups_details200response_ocs_data import (
    ProvisioningApiGroupsGetGroupsDetails200ResponseOcsData,
)


class ProvisioningApiGroupsGetGroupsDetails200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: ProvisioningApiGroupsGetGroupsDetails200ResponseOcsData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
