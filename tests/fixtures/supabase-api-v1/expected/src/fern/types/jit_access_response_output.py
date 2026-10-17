

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jit_access_response_output_user_roles_item import JitAccessResponseOutputUserRolesItem


class JitAccessResponseOutput(UniversalBaseModel):
    user_id: typing.Optional[str] = None
    user_roles: typing.List[JitAccessResponseOutputUserRolesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
