

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenScope(enum.StrEnum):
    """
    Scope of the token
    """

    READ = "read"
    WRITE = "write"

    def visit(self, read: typing.Callable[[], T_Result], write: typing.Callable[[], T_Result]) -> T_Result:
        if self is TokenScope.READ:
            return read()
        if self is TokenScope.WRITE:
            return write()
