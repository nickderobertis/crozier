

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContentSubmissionStatus(enum.StrEnum):
    IN_REVIEW = "in_review"
    CHANGES_REQUESTED = "changes_requested"
    APPROVED = "approved"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"
    SUPERSEDED = "superseded"
    PUBLICATION_FAILED = "publication_failed"

    def visit(
        self,
        in_review: typing.Callable[[], T_Result],
        changes_requested: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        published: typing.Callable[[], T_Result],
        superseded: typing.Callable[[], T_Result],
        publication_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContentSubmissionStatus.IN_REVIEW:
            return in_review()
        if self is ContentSubmissionStatus.CHANGES_REQUESTED:
            return changes_requested()
        if self is ContentSubmissionStatus.APPROVED:
            return approved()
        if self is ContentSubmissionStatus.SCHEDULED:
            return scheduled()
        if self is ContentSubmissionStatus.PUBLISHED:
            return published()
        if self is ContentSubmissionStatus.SUPERSEDED:
            return superseded()
        if self is ContentSubmissionStatus.PUBLICATION_FAILED:
            return publication_failed()
