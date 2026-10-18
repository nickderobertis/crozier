

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_jit_access_body_roles_item_allowed_networks_allowed_cidrs_item import (
    UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem,
)
from .update_jit_access_body_roles_item_allowed_networks_allowed_cidrs_v6item import (
    UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item,
)


class UpdateJitAccessBodyRolesItemAllowedNetworks(UniversalBaseModel):
    allowed_cidrs: typing.Optional[typing.List[UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem]] = None
    allowed_cidrs_v6: typing.Optional[typing.List[UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
