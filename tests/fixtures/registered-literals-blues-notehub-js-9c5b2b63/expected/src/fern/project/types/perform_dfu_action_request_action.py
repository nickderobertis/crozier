

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PerformDfuActionRequestAction(enum.StrEnum):
    UPDATE = "update"
    CANCEL = "cancel"

    def visit(self, update: typing.Callable[[], T_Result], cancel: typing.Callable[[], T_Result]) -> T_Result:
        if self is PerformDfuActionRequestAction.UPDATE:
            return update()
        if self is PerformDfuActionRequestAction.CANCEL:
            return cancel()
