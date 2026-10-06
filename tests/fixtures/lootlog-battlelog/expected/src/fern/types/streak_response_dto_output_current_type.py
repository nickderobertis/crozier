

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StreakResponseDtoOutputCurrentType(enum.StrEnum):
    WINS = "wins"
    LOSSES = "losses"
    NONE = "none"

    def visit(
        self,
        wins: typing.Callable[[], T_Result],
        losses: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StreakResponseDtoOutputCurrentType.WINS:
            return wins()
        if self is StreakResponseDtoOutputCurrentType.LOSSES:
            return losses()
        if self is StreakResponseDtoOutputCurrentType.NONE:
            return none()
