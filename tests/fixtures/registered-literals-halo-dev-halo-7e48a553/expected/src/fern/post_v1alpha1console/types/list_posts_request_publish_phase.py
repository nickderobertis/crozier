

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListPostsRequestPublishPhase(enum.StrEnum):
    DRAFT = "DRAFT"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    PUBLISHED = "PUBLISHED"
    FAILED = "FAILED"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        pending_approval: typing.Callable[[], T_Result],
        published: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListPostsRequestPublishPhase.DRAFT:
            return draft()
        if self is ListPostsRequestPublishPhase.PENDING_APPROVAL:
            return pending_approval()
        if self is ListPostsRequestPublishPhase.PUBLISHED:
            return published()
        if self is ListPostsRequestPublishPhase.FAILED:
            return failed()
