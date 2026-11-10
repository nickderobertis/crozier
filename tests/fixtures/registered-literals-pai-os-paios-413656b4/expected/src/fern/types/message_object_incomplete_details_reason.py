

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageObjectIncompleteDetailsReason(enum.StrEnum):
    """
    The reason the message is incomplete.
    """

    CONTENT_FILTER = "content_filter"
    MAX_TOKENS = "max_tokens"
    RUN_CANCELLED = "run_cancelled"
    RUN_EXPIRED = "run_expired"
    RUN_FAILED = "run_failed"

    def visit(
        self,
        content_filter: typing.Callable[[], T_Result],
        max_tokens: typing.Callable[[], T_Result],
        run_cancelled: typing.Callable[[], T_Result],
        run_expired: typing.Callable[[], T_Result],
        run_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageObjectIncompleteDetailsReason.CONTENT_FILTER:
            return content_filter()
        if self is MessageObjectIncompleteDetailsReason.MAX_TOKENS:
            return max_tokens()
        if self is MessageObjectIncompleteDetailsReason.RUN_CANCELLED:
            return run_cancelled()
        if self is MessageObjectIncompleteDetailsReason.RUN_EXPIRED:
            return run_expired()
        if self is MessageObjectIncompleteDetailsReason.RUN_FAILED:
            return run_failed()
