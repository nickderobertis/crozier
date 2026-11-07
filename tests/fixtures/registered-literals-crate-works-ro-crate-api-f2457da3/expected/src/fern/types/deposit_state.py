

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DepositState(enum.StrEnum):
    """
    The deposit's lifecycle state. `open` - accepting staging calls; `finalising` - a finalise is in progress and staging calls are rejected with 409; `complete` - the RO-Crate's new version is published (terminal); `aborted` - explicitly aborted or expired, staged content discarded (terminal). A failed finalise returns the deposit to `open` with the failure recorded in `errors`.
    """

    OPEN = "open"
    FINALISING = "finalising"
    COMPLETE = "complete"
    ABORTED = "aborted"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        finalising: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        aborted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DepositState.OPEN:
            return open()
        if self is DepositState.FINALISING:
            return finalising()
        if self is DepositState.COMPLETE:
            return complete()
        if self is DepositState.ABORTED:
            return aborted()
