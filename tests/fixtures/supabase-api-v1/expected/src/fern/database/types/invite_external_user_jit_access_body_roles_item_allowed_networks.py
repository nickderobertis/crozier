

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .invite_external_user_jit_access_body_roles_item_allowed_networks_allowed_cidrs_item import (
    InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem,
)
from .invite_external_user_jit_access_body_roles_item_allowed_networks_allowed_cidrs_v6item import (
    InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item,
)


class InviteExternalUserJitAccessBodyRolesItemAllowedNetworks(UniversalBaseModel):
    allowed_cidrs: typing.Optional[
        typing.List[InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem]
    ] = None
    allowed_cidrs_v6: typing.Optional[
        typing.List[InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item]
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
