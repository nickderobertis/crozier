

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IngestionEventSixType(enum.StrEnum):
    EVENT_CREATE = "event-create"

    def visit(self, event_create: typing.Callable[[], T_Result]) -> T_Result:
        if self is IngestionEventSixType.EVENT_CREATE:
            return event_create()
