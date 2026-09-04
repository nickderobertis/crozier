

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PushedAuthorizationRequestRequestCodeChallengeMethod(enum.StrEnum):
    S256 = "S256"

    def visit(self, s256: typing.Callable[[], T_Result]) -> T_Result:
        if self is PushedAuthorizationRequestRequestCodeChallengeMethod.S256:
            return s256()
