

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PriorityPackagesGetPriorityPackagesRequestStatus(enum.StrEnum):
    ACTIVE = "Active"
    COMPLETED = "Completed"
    ALL = "All"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PriorityPackagesGetPriorityPackagesRequestStatus.ACTIVE:
            return active()
        if self is PriorityPackagesGetPriorityPackagesRequestStatus.COMPLETED:
            return completed()
        if self is PriorityPackagesGetPriorityPackagesRequestStatus.ALL:
            return all_()
