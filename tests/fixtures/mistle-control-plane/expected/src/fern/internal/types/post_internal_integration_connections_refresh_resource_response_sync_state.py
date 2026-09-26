

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalIntegrationConnectionsRefreshResourceResponseSyncState(enum.StrEnum):
    SYNCING = "syncing"

    def visit(self, syncing: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalIntegrationConnectionsRefreshResourceResponseSyncState.SYNCING:
            return syncing()
