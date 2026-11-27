

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntryReviewProcessType(enum.StrEnum):
    """
    Type of the Review Process
    """

    SELF_REVIEW = "SELF_REVIEW"
    SEQUENTIAL = "SEQUENTIAL"
    PARALLEL = "PARALLEL"

    def visit(
        self,
        self_review: typing.Callable[[], T_Result],
        sequential: typing.Callable[[], T_Result],
        parallel: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntryReviewProcessType.SELF_REVIEW:
            return self_review()
        if self is EntryReviewProcessType.SEQUENTIAL:
            return sequential()
        if self is EntryReviewProcessType.PARALLEL:
            return parallel()
