

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ThreadTtlStrategy(enum.StrEnum):
    """
    The TTL strategy.
    """

    DELETE = "delete"
    KEEP_LATEST = "keep_latest"

    def visit(self, delete: typing.Callable[[], T_Result], keep_latest: typing.Callable[[], T_Result]) -> T_Result:
        if self is ThreadTtlStrategy.DELETE:
            return delete()
        if self is ThreadTtlStrategy.KEEP_LATEST:
            return keep_latest()
