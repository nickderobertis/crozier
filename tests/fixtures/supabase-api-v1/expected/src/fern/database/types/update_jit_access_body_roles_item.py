

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_jit_access_body_roles_item_allowed_networks import UpdateJitAccessBodyRolesItemAllowedNetworks


class UpdateJitAccessBodyRolesItem(UniversalBaseModel):
    role: str
    expires_at: typing.Optional[float] = None
    allowed_networks: typing.Optional[UpdateJitAccessBodyRolesItemAllowedNetworks] = None
    branches_only: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
