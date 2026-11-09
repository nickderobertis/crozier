

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenRequestTokenScope(enum.StrEnum):
    """
    The scope of the token.
    """

    READ = "read"
    WRITE = "write"

    def visit(self, read: typing.Callable[[], T_Result], write: typing.Callable[[], T_Result]) -> T_Result:
        if self is TokenRequestTokenScope.READ:
            return read()
        if self is TokenRequestTokenScope.WRITE:
            return write()
