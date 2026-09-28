

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreemptionStatusState(enum.StrEnum):
    INACTIVE = "inactive"
    DRAINING = "draining"
    DRAINED = "drained"

    def visit(
        self,
        inactive: typing.Callable[[], T_Result],
        draining: typing.Callable[[], T_Result],
        drained: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PreemptionStatusState.INACTIVE:
            return inactive()
        if self is PreemptionStatusState.DRAINING:
            return draining()
        if self is PreemptionStatusState.DRAINED:
            return drained()
