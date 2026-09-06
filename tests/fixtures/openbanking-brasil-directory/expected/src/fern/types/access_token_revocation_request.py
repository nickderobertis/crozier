

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_token_revocation_request_token_type_hint import AccessTokenRevocationRequestTokenTypeHint


class AccessTokenRevocationRequest(UniversalBaseModel):
    """
    A valid RFC7009 request - https://datatracker.ietf.org/doc/html/rfc7009#section-2.1
    """

    token: str = pydantic.Field()
    """
    The token that the client wants to get revoked.
    """

    token_type_hint: typing.Optional[AccessTokenRevocationRequestTokenTypeHint] = pydantic.Field(default=None)
    """
    A hint about the type of the token
    submitted for revocation.  Clients MAY pass this parameter in
    order to help the authorization server to optimize the token
    lookup.  If the server is unable to locate the token using
    the given hint, it MUST extend its search across all of its
    supported token types.  An authorization server MAY ignore
    this parameter, particularly if it is able to detect the
    token type automatically.  This specification defines two
    such values:
    
    * access_token: An access token as defined in [RFC6749],
      Section 1.4
    
    * refresh_token: A refresh token as defined in [RFC6749],
      Section 1.5
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
