

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeAgentUpgradeStatusPhase(enum.StrEnum):
    """
    Pending before installation starts. Running includes retries.
    """

    PENDING = "Pending"
    RUNNING = "Running"

    def visit(self, pending: typing.Callable[[], T_Result], running: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeAgentUpgradeStatusPhase.PENDING:
            return pending()
        if self is NodeAgentUpgradeStatusPhase.RUNNING:
            return running()
