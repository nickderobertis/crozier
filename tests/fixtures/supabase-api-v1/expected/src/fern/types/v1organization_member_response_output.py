

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1OrganizationMemberResponseOutput(UniversalBaseModel):
    user_id: str
    user_name: str
    email: typing.Optional[str] = None
    role_name: typing.Optional[str] = None
    mfa_enabled: bool
    avatar_url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
