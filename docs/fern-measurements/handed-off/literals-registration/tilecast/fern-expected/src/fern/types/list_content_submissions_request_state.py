

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListContentSubmissionsRequestState(enum.StrEnum):
    IN_REVIEW = "in_review"
    CHANGES_REQUESTED = "changes_requested"
    APPROVED = "approved"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"
    PUBLICATION_FAILED = "publication_failed"
    SUPERSEDED = "superseded"

    def visit(
        self,
        in_review: typing.Callable[[], T_Result],
        changes_requested: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        published: typing.Callable[[], T_Result],
        publication_failed: typing.Callable[[], T_Result],
        superseded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListContentSubmissionsRequestState.IN_REVIEW:
            return in_review()
        if self is ListContentSubmissionsRequestState.CHANGES_REQUESTED:
            return changes_requested()
        if self is ListContentSubmissionsRequestState.APPROVED:
            return approved()
        if self is ListContentSubmissionsRequestState.SCHEDULED:
            return scheduled()
        if self is ListContentSubmissionsRequestState.PUBLISHED:
            return published()
        if self is ListContentSubmissionsRequestState.PUBLICATION_FAILED:
            return publication_failed()
        if self is ListContentSubmissionsRequestState.SUPERSEDED:
            return superseded()
