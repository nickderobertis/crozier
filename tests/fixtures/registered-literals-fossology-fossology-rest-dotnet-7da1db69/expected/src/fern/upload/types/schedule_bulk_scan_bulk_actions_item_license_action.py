

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleBulkScanBulkActionsItemLicenseAction(enum.StrEnum):
    ADD = "ADD"
    REMOVE = "REMOVE"

    def visit(self, add: typing.Callable[[], T_Result], remove: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScheduleBulkScanBulkActionsItemLicenseAction.ADD:
            return add()
        if self is ScheduleBulkScanBulkActionsItemLicenseAction.REMOVE:
            return remove()
