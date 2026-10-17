

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ThreadPruneRequestStrategy(enum.StrEnum):
    """
    The prune strategy. 'delete' removes threads entirely. 'keep_latest' prunes old checkpoints but keeps threads and their latest state.
    """

    DELETE = "delete"
    KEEP_LATEST = "keep_latest"

    def visit(self, delete: typing.Callable[[], T_Result], keep_latest: typing.Callable[[], T_Result]) -> T_Result:
        if self is ThreadPruneRequestStrategy.DELETE:
            return delete()
        if self is ThreadPruneRequestStrategy.KEEP_LATEST:
            return keep_latest()
