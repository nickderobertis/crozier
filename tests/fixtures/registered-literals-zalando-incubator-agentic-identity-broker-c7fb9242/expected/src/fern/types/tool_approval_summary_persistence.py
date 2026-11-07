

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolApprovalSummaryPersistence(enum.StrEnum):
    ONCE = "once"
    SESSION = "session"
    PERMANENT = "permanent"

    def visit(
        self,
        once: typing.Callable[[], T_Result],
        session: typing.Callable[[], T_Result],
        permanent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ToolApprovalSummaryPersistence.ONCE:
            return once()
        if self is ToolApprovalSummaryPersistence.SESSION:
            return session()
        if self is ToolApprovalSummaryPersistence.PERMANENT:
            return permanent()
