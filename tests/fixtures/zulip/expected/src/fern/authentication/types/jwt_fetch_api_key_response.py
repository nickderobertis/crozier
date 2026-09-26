

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .jwt_fetch_api_key_response_user import JwtFetchApiKeyResponseUser


class JwtFetchApiKeyResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    api_key: str = pydantic.Field()
    """
    The API key that can be used to authenticate as the requested user.
    """

    email: str = pydantic.Field()
    """
    The email address of the user who owns the API key.
    """

    user: typing.Optional[JwtFetchApiKeyResponseUser] = pydantic.Field(default=None)
    """
    Only present if `include_profile` parameter was set to `true`.
    
    A dictionary with data on the target user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
