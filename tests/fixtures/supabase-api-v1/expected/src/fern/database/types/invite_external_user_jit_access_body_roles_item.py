

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .invite_external_user_jit_access_body_roles_item_allowed_networks import (
    InviteExternalUserJitAccessBodyRolesItemAllowedNetworks,
)


class InviteExternalUserJitAccessBodyRolesItem(UniversalBaseModel):
    role: str
    expires_at: typing.Optional[float] = None
    allowed_networks: typing.Optional[InviteExternalUserJitAccessBodyRolesItemAllowedNetworks] = None
    branches_only: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
