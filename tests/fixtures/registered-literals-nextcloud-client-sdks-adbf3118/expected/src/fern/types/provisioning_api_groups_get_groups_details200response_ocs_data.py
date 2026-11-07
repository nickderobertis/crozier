

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provisioning_api_group_details import ProvisioningApiGroupDetails


class ProvisioningApiGroupsGetGroupsDetails200ResponseOcsData(UniversalBaseModel):
    groups: typing.List[ProvisioningApiGroupDetails]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
