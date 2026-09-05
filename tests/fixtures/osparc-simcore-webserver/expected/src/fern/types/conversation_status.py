

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConversationStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"

    def visit(self, active: typing.Callable[[], T_Result], archived: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConversationStatus.ACTIVE:
            return active()
        if self is ConversationStatus.ARCHIVED:
            return archived()
