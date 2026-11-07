

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExpandableExpenseStatus(enum.StrEnum):
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
        if self is ExpandableExpenseStatus.DRAFT:
            return draft()
        if self is ExpandableExpenseStatus.SUBMITTED:
            return submitted()
        if self is ExpandableExpenseStatus.APPROVED:
            return approved()
        if self is ExpandableExpenseStatus.OUT_OF_POLICY:
            return out_of_policy()
        if self is ExpandableExpenseStatus.VOID:
            return void()
        if self is ExpandableExpenseStatus.CANCELED:
            return canceled()
        if self is ExpandableExpenseStatus.SPLIT:
            return split()
        if self is ExpandableExpenseStatus.SETTLED:
            return settled()
