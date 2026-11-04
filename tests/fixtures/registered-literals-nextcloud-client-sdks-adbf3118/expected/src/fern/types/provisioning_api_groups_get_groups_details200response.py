

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provisioning_api_groups_get_groups_details200response_ocs import (
    ProvisioningApiGroupsGetGroupsDetails200ResponseOcs,
)


class ProvisioningApiGroupsGetGroupsDetails200Response(UniversalBaseModel):
    ocs: ProvisioningApiGroupsGetGroupsDetails200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
