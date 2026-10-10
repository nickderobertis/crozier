

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RelayStateState(enum.StrEnum):
    ENERGISED = "energised"
    RELEASED = "released"
    FAULT = "fault"

    def visit(
        self,
        energised: typing.Callable[[], T_Result],
        released: typing.Callable[[], T_Result],
        fault: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RelayStateState.ENERGISED:
            return energised()
        if self is RelayStateState.RELEASED:
            return released()
        if self is RelayStateState.FAULT:
            return fault()
