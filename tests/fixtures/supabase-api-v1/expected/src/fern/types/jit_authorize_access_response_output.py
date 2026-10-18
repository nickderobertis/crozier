

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jit_authorize_access_response_output_user_role import JitAuthorizeAccessResponseOutputUserRole


class JitAuthorizeAccessResponseOutput(UniversalBaseModel):
    user_id: str
    user_role: JitAuthorizeAccessResponseOutputUserRole

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
