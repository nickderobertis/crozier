

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModuleStatusLabel(enum.StrEnum):
    OFFLINE = "Offline"
    ACTIVE = "Active"
    PLANNED = "Planned"
    STAGED = "Staged"
    FAILED = "Failed"
    DECOMMISSIONING = "Decommissioning"

    def visit(
        self,
        offline: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        staged: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        decommissioning: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ModuleStatusLabel.OFFLINE:
            return offline()
        if self is ModuleStatusLabel.ACTIVE:
            return active()
        if self is ModuleStatusLabel.PLANNED:
            return planned()
        if self is ModuleStatusLabel.STAGED:
            return staged()
        if self is ModuleStatusLabel.FAILED:
            return failed()
        if self is ModuleStatusLabel.DECOMMISSIONING:
            return decommissioning()
