

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CampaignBlockType(enum.StrEnum):
    ONE_TIME = "one_time"
    WEEKLY = "weekly"

    def visit(self, one_time: typing.Callable[[], T_Result], weekly: typing.Callable[[], T_Result]) -> T_Result:
        if self is CampaignBlockType.ONE_TIME:
            return one_time()
        if self is CampaignBlockType.WEEKLY:
            return weekly()
