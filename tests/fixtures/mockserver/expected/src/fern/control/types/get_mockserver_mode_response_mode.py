

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetMockserverModeResponseMode(enum.StrEnum):
    SIMULATE = "SIMULATE"
    SPY = "SPY"
    CAPTURE = "CAPTURE"

    def visit(
        self,
        simulate: typing.Callable[[], T_Result],
        spy: typing.Callable[[], T_Result],
        capture: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetMockserverModeResponseMode.SIMULATE:
            return simulate()
        if self is GetMockserverModeResponseMode.SPY:
            return spy()
        if self is GetMockserverModeResponseMode.CAPTURE:
            return capture()
