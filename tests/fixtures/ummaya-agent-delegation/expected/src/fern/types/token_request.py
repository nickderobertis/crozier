

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .token_request_grant_type import TokenRequestGrantType


class TokenRequest(UniversalBaseModel):
    grant_type: TokenRequestGrantType = pydantic.Field()
    """
    Device grant (RFC 8628) or token exchange (RFC 8693).
    """

    code_verifier: str = pydantic.Field()
    """
    PKCE code verifier (RFC 7636).
    """

    device_code: typing.Optional[str] = None
    subject_token: typing.Optional[str] = None
    subject_token_type: typing.Optional[str] = None
    audience: typing.Optional[str] = None
    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    Space-separated scope string.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
