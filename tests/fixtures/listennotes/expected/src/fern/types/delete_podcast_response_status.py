

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeletePodcastResponseStatus(enum.StrEnum):
    """
    The status of this podcast deletion request.
    """

    DELETED = "deleted"
    IN_REVIEW = "in review"

    def visit(self, deleted: typing.Callable[[], T_Result], in_review: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeletePodcastResponseStatus.DELETED:
            return deleted()
        if self is DeletePodcastResponseStatus.IN_REVIEW:
            return in_review()
