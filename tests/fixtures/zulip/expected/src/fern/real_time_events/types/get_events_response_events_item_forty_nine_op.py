

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFortyNineOp(enum.StrEnum):
    REMOVE_SUBGROUPS = "remove_subgroups"

    def visit(self, remove_subgroups: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFortyNineOp.REMOVE_SUBGROUPS:
            return remove_subgroups()
