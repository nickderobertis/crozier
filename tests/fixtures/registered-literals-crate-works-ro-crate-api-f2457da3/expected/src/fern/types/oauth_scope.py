

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    READ = "read"
    """
    Grants read access
    """

    WRITE = "write"
    """
    Grants write access through deposit sessions. Finer-grained authorisation policy is implementation-defined.
    """

    def visit(self, read: typing.Callable[[], T_Result], write: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.READ:
            return read()
        if self is OauthScope.WRITE:
            return write()
