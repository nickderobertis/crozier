

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jit_list_access_response_output_items_item_one_user_roles_item import (
    JitListAccessResponseOutputItemsItemOneUserRolesItem,
)


class JitListAccessResponseOutputItemsItemOne(UniversalBaseModel):
    user_id: typing.Optional[typing.Any] = None
    primary_email: str
    invite_id: str
    expires_at: str
    user_roles: typing.List[JitListAccessResponseOutputItemsItemOneUserRolesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
