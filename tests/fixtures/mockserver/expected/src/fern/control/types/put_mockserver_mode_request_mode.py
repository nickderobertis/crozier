

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverModeRequestMode(enum.StrEnum):
    SIMULATE = "SIMULATE"
    SPY = "SPY"
    CAPTURE = "CAPTURE"

    def visit(
        self,
        simulate: typing.Callable[[], T_Result],
        spy: typing.Callable[[], T_Result],
        capture: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PutMockserverModeRequestMode.SIMULATE:
            return simulate()
        if self is PutMockserverModeRequestMode.SPY:
            return spy()
        if self is PutMockserverModeRequestMode.CAPTURE:
            return capture()
