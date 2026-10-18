

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod(enum.StrEnum):
    PLAIN = "plain"
    SHA256 = "sha256"
    S256 = "S256"

    def visit(
        self,
        plain: typing.Callable[[], T_Result],
        sha256: typing.Callable[[], T_Result],
        s256: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod.PLAIN:
            return plain()
        if self is V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod.SHA256:
            return sha256()
        if self is V1OauthAuthorizeProjectClaimRequestCodeChallengeMethod.S256:
            return s256()
