

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ThreadPatchTtlStrategy(enum.StrEnum):
    """
    The TTL strategy. 'delete' removes the entire thread. 'keep_latest' prunes old checkpoints but keeps the thread and its latest state.
    """

    DELETE = "delete"
    KEEP_LATEST = "keep_latest"

    def visit(self, delete: typing.Callable[[], T_Result], keep_latest: typing.Callable[[], T_Result]) -> T_Result:
        if self is ThreadPatchTtlStrategy.DELETE:
            return delete()
        if self is ThreadPatchTtlStrategy.KEEP_LATEST:
            return keep_latest()
