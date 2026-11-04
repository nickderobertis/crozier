

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListSinglePagesRequestPublishPhase(enum.StrEnum):
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
        if self is ListSinglePagesRequestPublishPhase.DRAFT:
            return draft()
        if self is ListSinglePagesRequestPublishPhase.PENDING_APPROVAL:
            return pending_approval()
        if self is ListSinglePagesRequestPublishPhase.PUBLISHED:
            return published()
        if self is ListSinglePagesRequestPublishPhase.FAILED:
            return failed()
