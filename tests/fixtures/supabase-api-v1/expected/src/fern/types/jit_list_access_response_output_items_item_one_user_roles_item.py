

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jit_list_access_response_output_items_item_one_user_roles_item_allowed_networks import (
    JitListAccessResponseOutputItemsItemOneUserRolesItemAllowedNetworks,
)


class JitListAccessResponseOutputItemsItemOneUserRolesItem(UniversalBaseModel):
    role: str
    expires_at: typing.Optional[float] = None
    allowed_networks: typing.Optional[JitListAccessResponseOutputItemsItemOneUserRolesItemAllowedNetworks] = None
    branches_only: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
