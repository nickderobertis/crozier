

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubmitPodcastResponseStatus(enum.StrEnum):
    """
    The status of this submission.
    """

    FOUND = "found"
    IN_REVIEW = "in review"
    REJECTED = "rejected"

    def visit(
        self,
        found: typing.Callable[[], T_Result],
        in_review: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubmitPodcastResponseStatus.FOUND:
            return found()
        if self is SubmitPodcastResponseStatus.IN_REVIEW:
            return in_review()
        if self is SubmitPodcastResponseStatus.REJECTED:
            return rejected()
