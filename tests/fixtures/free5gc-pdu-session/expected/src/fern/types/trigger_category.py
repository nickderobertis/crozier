

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TriggerCategory(enum.StrEnum):
    IMMEDIATE_REPORT = "IMMEDIATE_REPORT"
    DEFERRED_REPORT = "DEFERRED_REPORT"

    def visit(
        self, immediate_report: typing.Callable[[], T_Result], deferred_report: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TriggerCategory.IMMEDIATE_REPORT:
            return immediate_report()
        if self is TriggerCategory.DEFERRED_REPORT:
            return deferred_report()
