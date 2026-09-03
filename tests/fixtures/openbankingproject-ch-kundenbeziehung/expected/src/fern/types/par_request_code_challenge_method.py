

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParRequestCodeChallengeMethod(enum.StrEnum):
    """
    PKCE code challenge method (S256 required)
    """

    S256 = "S256"

    def visit(self, s256: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParRequestCodeChallengeMethod.S256:
            return s256()
