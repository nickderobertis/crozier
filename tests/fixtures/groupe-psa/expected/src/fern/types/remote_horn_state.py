

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteHornState(enum.StrEnum):
    """
    Activate or unactivate this remote horn.
    """

    ACTIVATED = "Activated"
    UNACTIVATED = "Unactivated"

    def visit(self, activated: typing.Callable[[], T_Result], unactivated: typing.Callable[[], T_Result]) -> T_Result:
        if self is RemoteHornState.ACTIVATED:
            return activated()
        if self is RemoteHornState.UNACTIVATED:
            return unactivated()
