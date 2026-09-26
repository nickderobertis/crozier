

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemDraftIdOp(enum.StrEnum):
    REMOVE = "remove"

    def visit(self, remove: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemDraftIdOp.REMOVE:
            return remove()
