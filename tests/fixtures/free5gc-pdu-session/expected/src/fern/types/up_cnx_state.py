

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpCnxState(enum.StrEnum):
    ACTIVATED = "ACTIVATED"
    DEACTIVATED = "DEACTIVATED"
    ACTIVATING = "ACTIVATING"

    def visit(
        self,
        activated: typing.Callable[[], T_Result],
        deactivated: typing.Callable[[], T_Result],
        activating: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpCnxState.ACTIVATED:
            return activated()
        if self is UpCnxState.DEACTIVATED:
            return deactivated()
        if self is UpCnxState.ACTIVATING:
            return activating()
