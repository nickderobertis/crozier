

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ApproveRequestPersistence(enum.StrEnum):
    ONCE = "once"
    SESSION = "session"
    PERMANENT = "permanent"

    def visit(
        self,
        once: typing.Callable[[], T_Result],
        session: typing.Callable[[], T_Result],
        permanent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApproveRequestPersistence.ONCE:
            return once()
        if self is ApproveRequestPersistence.SESSION:
            return session()
        if self is ApproveRequestPersistence.PERMANENT:
            return permanent()
