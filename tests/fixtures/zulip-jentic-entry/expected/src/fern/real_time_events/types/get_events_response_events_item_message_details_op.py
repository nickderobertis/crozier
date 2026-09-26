

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemMessageDetailsOp(enum.StrEnum):
    REMOVE = "remove"

    def visit(self, remove: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemMessageDetailsOp.REMOVE:
            return remove()
