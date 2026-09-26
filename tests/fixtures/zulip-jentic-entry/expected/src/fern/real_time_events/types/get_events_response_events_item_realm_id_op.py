

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemRealmIdOp(enum.StrEnum):
    DEACTIVATED = "deactivated"

    def visit(self, deactivated: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemRealmIdOp.DEACTIVATED:
            return deactivated()
