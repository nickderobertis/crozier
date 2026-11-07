

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RepositoryTokenRequestIntent(enum.StrEnum):
    """
    Access intent for the vended credentials. Only `read` is
    supported today; `write` and `admin` are reserved for future use.
    """

    READ = "read"

    def visit(self, read: typing.Callable[[], T_Result]) -> T_Result:
        if self is RepositoryTokenRequestIntent.READ:
            return read()
