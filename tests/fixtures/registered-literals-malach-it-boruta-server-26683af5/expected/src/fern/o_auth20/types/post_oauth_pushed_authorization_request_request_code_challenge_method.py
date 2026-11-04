

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod(enum.StrEnum):
    PLAIN = "plain"
    S256 = "S256"

    def visit(self, plain: typing.Callable[[], T_Result], s256: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod.PLAIN:
            return plain()
        if self is PostOauthPushedAuthorizationRequestRequestCodeChallengeMethod.S256:
            return s256()
