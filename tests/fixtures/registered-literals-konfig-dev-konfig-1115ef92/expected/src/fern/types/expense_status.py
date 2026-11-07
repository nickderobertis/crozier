

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExpenseStatus(enum.StrEnum):
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    APPROVED = "APPROVED"
    OUT_OF_POLICY = "OUT_OF_POLICY"
    VOID = "VOID"
    CANCELED = "CANCELED"
    SPLIT = "SPLIT"
    SETTLED = "SETTLED"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        submitted: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        out_of_policy: typing.Callable[[], T_Result],
        void: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        split: typing.Callable[[], T_Result],
        settled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExpenseStatus.DRAFT:
            return draft()
        if self is ExpenseStatus.SUBMITTED:
            return submitted()
        if self is ExpenseStatus.APPROVED:
            return approved()
        if self is ExpenseStatus.OUT_OF_POLICY:
            return out_of_policy()
        if self is ExpenseStatus.VOID:
            return void()
        if self is ExpenseStatus.CANCELED:
            return canceled()
        if self is ExpenseStatus.SPLIT:
            return split()
        if self is ExpenseStatus.SETTLED:
            return settled()
