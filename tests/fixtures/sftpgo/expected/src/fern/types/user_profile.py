

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserProfile(UniversalBaseModel):
    email: typing.Optional[str] = None
    description: typing.Optional[str] = None
    allow_api_key_auth: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If enabled, you can impersonate this user, in REST API, using an API key. If disabled user credentials are required for impersonation
    """

    public_keys: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
