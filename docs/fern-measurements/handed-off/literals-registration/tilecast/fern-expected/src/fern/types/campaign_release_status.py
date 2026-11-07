

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CampaignReleaseStatus(enum.StrEnum):
    IN_REVIEW = "in_review"
    CHANGES_REQUESTED = "changes_requested"
    APPROVED = "approved"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"
    SUPERSEDED = "superseded"
    CANCELLED = "cancelled"
    PUBLICATION_FAILED = "publication_failed"

    def visit(
        self,
        in_review: typing.Callable[[], T_Result],
        changes_requested: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        published: typing.Callable[[], T_Result],
        superseded: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        publication_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CampaignReleaseStatus.IN_REVIEW:
            return in_review()
        if self is CampaignReleaseStatus.CHANGES_REQUESTED:
            return changes_requested()
        if self is CampaignReleaseStatus.APPROVED:
            return approved()
        if self is CampaignReleaseStatus.SCHEDULED:
            return scheduled()
        if self is CampaignReleaseStatus.PUBLISHED:
            return published()
        if self is CampaignReleaseStatus.SUPERSEDED:
            return superseded()
        if self is CampaignReleaseStatus.CANCELLED:
            return cancelled()
        if self is CampaignReleaseStatus.PUBLICATION_FAILED:
            return publication_failed()
