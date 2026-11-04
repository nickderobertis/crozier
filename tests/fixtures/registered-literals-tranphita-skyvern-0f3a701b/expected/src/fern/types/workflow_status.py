

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowStatus(enum.StrEnum):
    PUBLISHED = "published"
    DRAFT = "draft"
    AUTO_GENERATED = "auto_generated"

    def visit(
        self,
        published: typing.Callable[[], T_Result],
        draft: typing.Callable[[], T_Result],
        auto_generated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkflowStatus.PUBLISHED:
            return published()
        if self is WorkflowStatus.DRAFT:
            return draft()
        if self is WorkflowStatus.AUTO_GENERATED:
            return auto_generated()
