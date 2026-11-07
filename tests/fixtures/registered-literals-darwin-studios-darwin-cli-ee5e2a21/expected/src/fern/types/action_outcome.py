

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionOutcome(enum.StrEnum):
    """
    A bounded terminal classification. Unknown and censored outcomes are never silently relabeled as failures.
    """

    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELED = "canceled"
    UNKNOWN = "unknown"

    def visit(
        self,
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActionOutcome.SUCCEEDED:
            return succeeded()
        if self is ActionOutcome.FAILED:
            return failed()
        if self is ActionOutcome.CANCELED:
            return canceled()
        if self is ActionOutcome.UNKNOWN:
            return unknown()
