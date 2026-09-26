

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFortySevenOp(enum.StrEnum):
    REMOVE_MEMBERS = "remove_members"

    def visit(self, remove_members: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFortySevenOp.REMOVE_MEMBERS:
            return remove_members()
