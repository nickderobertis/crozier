

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .invite_external_user_jit_response_output_user_roles_item_allowed_networks_allowed_cidrs_item import (
    InviteExternalUserJitResponseOutputUserRolesItemAllowedNetworksAllowedCidrsItem,
)
from .invite_external_user_jit_response_output_user_roles_item_allowed_networks_allowed_cidrs_v6item import (
    InviteExternalUserJitResponseOutputUserRolesItemAllowedNetworksAllowedCidrsV6Item,
)


class InviteExternalUserJitResponseOutputUserRolesItemAllowedNetworks(UniversalBaseModel):
    allowed_cidrs: typing.Optional[
        typing.List[InviteExternalUserJitResponseOutputUserRolesItemAllowedNetworksAllowedCidrsItem]
    ] = None
    allowed_cidrs_v6: typing.Optional[
        typing.List[InviteExternalUserJitResponseOutputUserRolesItemAllowedNetworksAllowedCidrsV6Item]
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
