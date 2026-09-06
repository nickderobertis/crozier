

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccessTokenRevocationRequestTokenTypeHint(enum.StrEnum):
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

    ACCESS_TOKEN = "access_token"
    REFRESH_TOKEN = "refresh_token"

    def visit(
        self, access_token: typing.Callable[[], T_Result], refresh_token: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AccessTokenRevocationRequestTokenTypeHint.ACCESS_TOKEN:
            return access_token()
        if self is AccessTokenRevocationRequestTokenTypeHint.REFRESH_TOKEN:
            return refresh_token()
