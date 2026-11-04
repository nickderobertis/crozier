

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActUpdateRequestReasonCodeKind(enum.StrEnum):
    SAFETY_REPORT = "safety_report"

    def visit(self, safety_report: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActUpdateRequestReasonCodeKind.SAFETY_REPORT:
            return safety_report()
