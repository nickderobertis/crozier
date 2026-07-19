

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventMessageEventType(enum.StrEnum):
    COMPACTION = "compaction"

    def visit(self, compaction: typing.Callable[[], T_Result]) -> T_Result:
        if self is EventMessageEventType.COMPACTION:
            return compaction()
