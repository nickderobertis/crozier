

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SyncGraphCommandType(enum.StrEnum):
    SYNC_GRAPH = "sync-graph"

    def visit(self, sync_graph: typing.Callable[[], T_Result]) -> T_Result:
        if self is SyncGraphCommandType.SYNC_GRAPH:
            return sync_graph()
