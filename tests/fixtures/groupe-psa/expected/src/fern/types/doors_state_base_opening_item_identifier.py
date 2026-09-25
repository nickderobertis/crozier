

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DoorsStateBaseOpeningItemIdentifier(enum.StrEnum):
    DRIVER = "Driver"
    PASSENGER = "Passenger"
    REAR_LEFT = "RearLeft"
    REAR_RIGHT = "RearRight"
    TRUNK = "Trunk"
    REAR_WINDOW = "RearWindow"
    ROOF_WINDOW = "RoofWindow"

    def visit(
        self,
        driver: typing.Callable[[], T_Result],
        passenger: typing.Callable[[], T_Result],
        rear_left: typing.Callable[[], T_Result],
        rear_right: typing.Callable[[], T_Result],
        trunk: typing.Callable[[], T_Result],
        rear_window: typing.Callable[[], T_Result],
        roof_window: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DoorsStateBaseOpeningItemIdentifier.DRIVER:
            return driver()
        if self is DoorsStateBaseOpeningItemIdentifier.PASSENGER:
            return passenger()
        if self is DoorsStateBaseOpeningItemIdentifier.REAR_LEFT:
            return rear_left()
        if self is DoorsStateBaseOpeningItemIdentifier.REAR_RIGHT:
            return rear_right()
        if self is DoorsStateBaseOpeningItemIdentifier.TRUNK:
            return trunk()
        if self is DoorsStateBaseOpeningItemIdentifier.REAR_WINDOW:
            return rear_window()
        if self is DoorsStateBaseOpeningItemIdentifier.ROOF_WINDOW:
            return roof_window()
