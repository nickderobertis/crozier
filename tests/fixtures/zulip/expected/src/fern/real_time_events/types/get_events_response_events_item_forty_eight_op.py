

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFortyEightOp(enum.StrEnum):
    ADD_SUBGROUPS = "add_subgroups"

    def visit(self, add_subgroups: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFortyEightOp.ADD_SUBGROUPS:
            return add_subgroups()
