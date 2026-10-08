

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetSettingsResponseLight(enum.StrEnum):
    DAY = "day"
    NIGHT = "night"

    def visit(self, day: typing.Callable[[], T_Result], night: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetSettingsResponseLight.DAY:
            return day()
        if self is GetSettingsResponseLight.NIGHT:
            return night()
