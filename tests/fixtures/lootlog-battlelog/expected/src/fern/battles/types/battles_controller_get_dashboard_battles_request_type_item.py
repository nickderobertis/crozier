

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class BattlesControllerGetDashboardBattlesRequestTypeItem(enum.StrEnum):
    SOLO = "solo"
    GROUP = "group"

    def visit(self, solo: typing.Callable[[], T_Result], group: typing.Callable[[], T_Result]) -> T_Result:
        if self is BattlesControllerGetDashboardBattlesRequestTypeItem.SOLO:
            return solo()
        if self is BattlesControllerGetDashboardBattlesRequestTypeItem.GROUP:
            return group()
