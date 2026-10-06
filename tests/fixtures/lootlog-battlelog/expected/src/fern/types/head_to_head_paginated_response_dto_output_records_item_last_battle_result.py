

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleResult(enum.StrEnum):
    WON = "won"
    LOST = "lost"
    FLEE = "flee"

    def visit(
        self,
        won: typing.Callable[[], T_Result],
        lost: typing.Callable[[], T_Result],
        flee: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleResult.WON:
            return won()
        if self is HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleResult.LOST:
            return lost()
        if self is HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleResult.FLEE:
            return flee()
