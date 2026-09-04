

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostOauthParRequestCodeChallengeMethod(enum.StrEnum):
    """
    A method that was used to derive code challenge.
    """

    S256 = "S256"

    def visit(self, s256: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostOauthParRequestCodeChallengeMethod.S256:
            return s256()
