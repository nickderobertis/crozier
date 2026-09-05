

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchProjectAutomationConfigObjectTypeEventType(enum.StrEnum):
    """
    The type of automation.
    """

    RETENTION = "retention"

    def visit(self, retention: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchProjectAutomationConfigObjectTypeEventType.RETENTION:
            return retention()
