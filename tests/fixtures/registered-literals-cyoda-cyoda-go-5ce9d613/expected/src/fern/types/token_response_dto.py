

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .token_response_dto_issued_token_type import TokenResponseDtoIssuedTokenType
from .token_response_dto_token_type import TokenResponseDtoTokenType


class TokenResponseDto(UniversalBaseModel):
    access_token: str = pydantic.Field()
    """
    The JWT access token for API authentication
    """

    token_type: TokenResponseDtoTokenType = pydantic.Field()
    """
    The type of token issued (currently always 'Bearer')
    """

    expires_in: int = pydantic.Field()
    """
    The lifetime in seconds of the access token
    """

    refresh_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The refresh token for obtaining new access tokens
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    The scope of the access token, as per RFC 6749 Section 3.3. See https://datatracker.ietf.org/doc/html/rfc6749#section-3.3
    """

    issued_token_type: typing.Optional[TokenResponseDtoIssuedTokenType] = pydantic.Field(default=None)
    """
    The type of the issued token (present only for token-exchange responses, per RFC 8693)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
