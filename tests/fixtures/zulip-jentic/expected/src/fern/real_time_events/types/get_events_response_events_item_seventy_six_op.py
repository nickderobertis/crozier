

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemSeventySixOp(enum.StrEnum):
    UPDATE = "update"

    def visit(self, update: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemSeventySixOp.UPDATE:
            return update()
