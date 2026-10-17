

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .invite_external_user_jit_response_output_user_roles_item import InviteExternalUserJitResponseOutputUserRolesItem


class InviteExternalUserJitResponseOutput(UniversalBaseModel):
    email: str
    invite_id: str
    user_roles: typing.List[InviteExternalUserJitResponseOutputUserRolesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
