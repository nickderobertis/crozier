

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFortyFiveOp(enum.StrEnum):
    ADD_MEMBERS = "add_members"

    def visit(self, add_members: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFortyFiveOp.ADD_MEMBERS:
            return add_members()
