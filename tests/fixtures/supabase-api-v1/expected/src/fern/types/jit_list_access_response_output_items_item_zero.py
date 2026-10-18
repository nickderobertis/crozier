

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jit_list_access_response_output_items_item_zero_user_roles_item import (
    JitListAccessResponseOutputItemsItemZeroUserRolesItem,
)


class JitListAccessResponseOutputItemsItemZero(UniversalBaseModel):
    user_id: str
    primary_email: typing.Optional[str] = None
    invite_id: typing.Optional[typing.Any] = None
    expires_at: typing.Optional[typing.Any] = None
    user_roles: typing.List[JitListAccessResponseOutputItemsItemZeroUserRolesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
