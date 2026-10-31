

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DynamicSidecarStatus(enum.StrEnum):
    OK = "ok"
    FAILING = "failing"

    def visit(self, ok: typing.Callable[[], T_Result], failing: typing.Callable[[], T_Result]) -> T_Result:
        if self is DynamicSidecarStatus.OK:
            return ok()
        if self is DynamicSidecarStatus.FAILING:
            return failing()
