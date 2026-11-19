

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReconcileState(enum.StrEnum):
    """
    Result of reconciling the lineage graph's recorded version against the on-disk Lance version.
    """

    IN_SYNC = "in_sync"
    STORAGE_AHEAD = "storage_ahead"
    GRAPH_AHEAD = "graph_ahead"
    UNTRACKED = "untracked"
    MISSING_ON_STORAGE = "missing_on_storage"
    ABSENT = "absent"
    UNREADABLE = "unreadable"
    UNGOVERNED = "ungoverned"
    UNGOVERNED_LIVE = "ungoverned_live"
    DROP_OBSERVED = "drop_observed"

    def visit(
        self,
        in_sync: typing.Callable[[], T_Result],
        storage_ahead: typing.Callable[[], T_Result],
        graph_ahead: typing.Callable[[], T_Result],
        untracked: typing.Callable[[], T_Result],
        missing_on_storage: typing.Callable[[], T_Result],
        absent: typing.Callable[[], T_Result],
        unreadable: typing.Callable[[], T_Result],
        ungoverned: typing.Callable[[], T_Result],
        ungoverned_live: typing.Callable[[], T_Result],
        drop_observed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReconcileState.IN_SYNC:
            return in_sync()
        if self is ReconcileState.STORAGE_AHEAD:
            return storage_ahead()
        if self is ReconcileState.GRAPH_AHEAD:
            return graph_ahead()
        if self is ReconcileState.UNTRACKED:
            return untracked()
        if self is ReconcileState.MISSING_ON_STORAGE:
            return missing_on_storage()
        if self is ReconcileState.ABSENT:
            return absent()
        if self is ReconcileState.UNREADABLE:
            return unreadable()
        if self is ReconcileState.UNGOVERNED:
            return ungoverned()
        if self is ReconcileState.UNGOVERNED_LIVE:
            return ungoverned_live()
        if self is ReconcileState.DROP_OBSERVED:
            return drop_observed()
