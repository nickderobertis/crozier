

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jit_access_response_output_user_roles_item_allowed_networks_allowed_cidrs_item import (
    JitAccessResponseOutputUserRolesItemAllowedNetworksAllowedCidrsItem,
)
from .jit_access_response_output_user_roles_item_allowed_networks_allowed_cidrs_v6item import (
    JitAccessResponseOutputUserRolesItemAllowedNetworksAllowedCidrsV6Item,
)


class JitAccessResponseOutputUserRolesItemAllowedNetworks(UniversalBaseModel):
    allowed_cidrs: typing.Optional[typing.List[JitAccessResponseOutputUserRolesItemAllowedNetworksAllowedCidrsItem]] = (
        None
    )
    allowed_cidrs_v6: typing.Optional[
        typing.List[JitAccessResponseOutputUserRolesItemAllowedNetworksAllowedCidrsV6Item]
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
