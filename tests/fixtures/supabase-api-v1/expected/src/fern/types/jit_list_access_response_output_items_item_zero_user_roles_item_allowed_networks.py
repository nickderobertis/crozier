

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jit_list_access_response_output_items_item_zero_user_roles_item_allowed_networks_allowed_cidrs_item import (
    JitListAccessResponseOutputItemsItemZeroUserRolesItemAllowedNetworksAllowedCidrsItem,
)
from .jit_list_access_response_output_items_item_zero_user_roles_item_allowed_networks_allowed_cidrs_v6item import (
    JitListAccessResponseOutputItemsItemZeroUserRolesItemAllowedNetworksAllowedCidrsV6Item,
)


class JitListAccessResponseOutputItemsItemZeroUserRolesItemAllowedNetworks(UniversalBaseModel):
    allowed_cidrs: typing.Optional[
        typing.List[JitListAccessResponseOutputItemsItemZeroUserRolesItemAllowedNetworksAllowedCidrsItem]
    ] = None
    allowed_cidrs_v6: typing.Optional[
        typing.List[JitListAccessResponseOutputItemsItemZeroUserRolesItemAllowedNetworksAllowedCidrsV6Item]
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
