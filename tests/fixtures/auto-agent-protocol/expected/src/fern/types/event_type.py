

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventType(enum.StrEnum):
    AAP_EVENT = "aap.event"

    def visit(self, aap_event: typing.Callable[[], T_Result]) -> T_Result:
        if self is EventType.AAP_EVENT:
            return aap_event()
