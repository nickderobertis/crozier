

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetAuthorizationRequestCodeChallengeMethod(enum.StrEnum):
    S256 = "S256"
    PLAIN = "plain"

    def visit(self, s256: typing.Callable[[], T_Result], plain: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetAuthorizationRequestCodeChallengeMethod.S256:
            return s256()
        if self is GetAuthorizationRequestCodeChallengeMethod.PLAIN:
            return plain()
