

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubscribeToGameEventsResponseItemSixEvent(enum.StrEnum):
    PLAYER_CODE_REVEAL = "playerCodeReveal"

    def visit(self, player_code_reveal: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscribeToGameEventsResponseItemSixEvent.PLAYER_CODE_REVEAL:
            return player_code_reveal()
