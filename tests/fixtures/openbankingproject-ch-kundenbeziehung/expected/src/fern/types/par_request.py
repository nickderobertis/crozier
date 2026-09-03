

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .par_request_code_challenge_method import ParRequestCodeChallengeMethod
from .par_request_response_type import ParRequestResponseType


class ParRequest(UniversalBaseModel):
    client_id: str = pydantic.Field()
    """
    Client Identifier
    """

    response_type: ParRequestResponseType = pydantic.Field()
    """
    OAuth 2.1 response type (only code allowed)
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    OAuth scopes
    """

    redirect_uri: str = pydantic.Field()
    """
    Client redirect URI
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    OAuth state parameter
    """

    code_challenge: str = pydantic.Field()
    """
    PKCE code challenge (FAPI 2.0 required)
    """

    code_challenge_method: ParRequestCodeChallengeMethod = pydantic.Field()
    """
    PKCE code challenge method (S256 required)
    """

    nonce: typing.Optional[str] = pydantic.Field(default=None)
    """
    OpenID Connect nonce
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
