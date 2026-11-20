

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoomReadingTensionZero(enum.StrEnum):
    SLACK = "slack"
    EVEN = "even"
    TAUT = "taut"

    def visit(
        self,
        slack: typing.Callable[[], T_Result],
        even: typing.Callable[[], T_Result],
        taut: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoomReadingTensionZero.SLACK:
            return slack()
        if self is LoomReadingTensionZero.EVEN:
            return even()
        if self is LoomReadingTensionZero.TAUT:
            return taut()
