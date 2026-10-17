

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .o_auth_token_response_output_token_type import OAuthTokenResponseOutputTokenType


class OAuthTokenResponseOutput(UniversalBaseModel):
    access_token: str
    refresh_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `urn:ietf:params:oauth:grant-type:jwt-bearer` grant type issues access tokens only, no refresh token is returned and the token cannot be revoked via `/v1/oauth/revoke`.
    """

    expires_in: int
    token_type: OAuthTokenResponseOutputTokenType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
