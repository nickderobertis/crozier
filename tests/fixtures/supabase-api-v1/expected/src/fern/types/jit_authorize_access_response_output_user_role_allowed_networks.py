

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jit_authorize_access_response_output_user_role_allowed_networks_allowed_cidrs_item import (
    JitAuthorizeAccessResponseOutputUserRoleAllowedNetworksAllowedCidrsItem,
)
from .jit_authorize_access_response_output_user_role_allowed_networks_allowed_cidrs_v6item import (
    JitAuthorizeAccessResponseOutputUserRoleAllowedNetworksAllowedCidrsV6Item,
)


class JitAuthorizeAccessResponseOutputUserRoleAllowedNetworks(UniversalBaseModel):
    allowed_cidrs: typing.Optional[
        typing.List[JitAuthorizeAccessResponseOutputUserRoleAllowedNetworksAllowedCidrsItem]
    ] = None
    allowed_cidrs_v6: typing.Optional[
        typing.List[JitAuthorizeAccessResponseOutputUserRoleAllowedNetworksAllowedCidrsV6Item]
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
