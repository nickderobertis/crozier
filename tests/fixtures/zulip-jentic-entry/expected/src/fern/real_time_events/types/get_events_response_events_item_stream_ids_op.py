

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemStreamIdsOp(enum.StrEnum):
    DELETE = "delete"

    def visit(self, delete: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemStreamIdsOp.DELETE:
            return delete()
