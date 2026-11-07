

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubscribeToGameEventsResponseItemTenEvent(enum.StrEnum):
    ELIMINATED = "eliminated"

    def visit(self, eliminated: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscribeToGameEventsResponseItemTenEvent.ELIMINATED:
            return eliminated()
