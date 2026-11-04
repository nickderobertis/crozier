

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomPronunciationStatus(enum.StrEnum):
    """
    Processing status. Only "ready" pronunciations are applied during synthesis.
    """

    PENDING = "pending"
    READY = "ready"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomPronunciationStatus.PENDING:
            return pending()
        if self is CustomPronunciationStatus.READY:
            return ready()
        if self is CustomPronunciationStatus.FAILED:
            return failed()
