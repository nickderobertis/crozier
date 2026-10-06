

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class BattlesControllerGetBattleDurationRequestSortOrder(enum.StrEnum):
    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is BattlesControllerGetBattleDurationRequestSortOrder.ASC:
            return asc()
        if self is BattlesControllerGetBattleDurationRequestSortOrder.DESC:
            return desc()
