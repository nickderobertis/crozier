

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubscribeToGameEventsResponseItemFiveEvent(enum.StrEnum):
    PLAYER_SUBMIT = "playerSubmit"

    def visit(self, player_submit: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscribeToGameEventsResponseItemFiveEvent.PLAYER_SUBMIT:
            return player_submit()
