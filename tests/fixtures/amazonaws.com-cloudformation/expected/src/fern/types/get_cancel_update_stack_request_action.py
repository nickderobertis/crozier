

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetCancelUpdateStackRequestAction(enum.StrEnum):
    CANCEL_UPDATE_STACK = "CancelUpdateStack"

    def visit(self, cancel_update_stack: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCancelUpdateStackRequestAction.CANCEL_UPDATE_STACK:
            return cancel_update_stack()
