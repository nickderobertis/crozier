

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListMyPostsRequestPublishPhase(enum.StrEnum):
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
        if self is ListMyPostsRequestPublishPhase.DRAFT:
            return draft()
        if self is ListMyPostsRequestPublishPhase.PENDING_APPROVAL:
            return pending_approval()
        if self is ListMyPostsRequestPublishPhase.PUBLISHED:
            return published()
        if self is ListMyPostsRequestPublishPhase.FAILED:
            return failed()
