

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchProjectAutomationConfigBatchSizeEventType(enum.StrEnum):
    """
    The type of automation.
    """

    BTQL_EXPORT = "btql_export"

    def visit(self, btql_export: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchProjectAutomationConfigBatchSizeEventType.BTQL_EXPORT:
            return btql_export()
