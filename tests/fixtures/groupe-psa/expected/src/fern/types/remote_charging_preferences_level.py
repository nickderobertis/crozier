

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteChargingPreferencesLevel(enum.StrEnum):
    """
    Charging power level.
    """

    LEVEL1 = "Level1"
    LEVEL2 = "Level2"
    LEVEL3 = "Level3"
    LEVEL4 = "Level4"
    LEVEL5 = "Level5"

    def visit(
        self,
        level1: typing.Callable[[], T_Result],
        level2: typing.Callable[[], T_Result],
        level3: typing.Callable[[], T_Result],
        level4: typing.Callable[[], T_Result],
        level5: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RemoteChargingPreferencesLevel.LEVEL1:
            return level1()
        if self is RemoteChargingPreferencesLevel.LEVEL2:
            return level2()
        if self is RemoteChargingPreferencesLevel.LEVEL3:
            return level3()
        if self is RemoteChargingPreferencesLevel.LEVEL4:
            return level4()
        if self is RemoteChargingPreferencesLevel.LEVEL5:
            return level5()
