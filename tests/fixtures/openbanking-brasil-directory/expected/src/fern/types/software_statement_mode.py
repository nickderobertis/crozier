

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SoftwareStatementMode(enum.StrEnum):
    """
    Software Statement mode
    """

    LIVE = "Live"
    TEST = "Test"

    def visit(self, live: typing.Callable[[], T_Result], test: typing.Callable[[], T_Result]) -> T_Result:
        if self is SoftwareStatementMode.LIVE:
            return live()
        if self is SoftwareStatementMode.TEST:
            return test()
