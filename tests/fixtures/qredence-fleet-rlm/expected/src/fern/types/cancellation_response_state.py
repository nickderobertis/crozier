

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CancellationResponseState(enum.StrEnum):
    REQUESTED = "requested"
    ALREADY_REQUESTED = "already_requested"
    ALREADY_TERMINAL = "already_terminal"

    def visit(
        self,
        requested: typing.Callable[[], T_Result],
        already_requested: typing.Callable[[], T_Result],
        already_terminal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CancellationResponseState.REQUESTED:
            return requested()
        if self is CancellationResponseState.ALREADY_REQUESTED:
            return already_requested()
        if self is CancellationResponseState.ALREADY_TERMINAL:
            return already_terminal()
