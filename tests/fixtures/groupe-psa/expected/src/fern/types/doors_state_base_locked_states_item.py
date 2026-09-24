

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DoorsStateBaseLockedStatesItem(enum.StrEnum):
    UNLOCKED = "Unlocked"
    LOCKED = "Locked"
    SUPER_LOCKED = "SuperLocked"
    DRIVER_DOOR_UNLOCKED = "DriverDoorUnlocked"
    CABIN_DOORS_UNLOCKED = "CabinDoorsUnlocked"
    CARGO_DOORS_LOCKED = "CargoDoorsLocked"
    CARGO_DOORS_UNLOCKED = "CargoDoorsUnlocked"
    REAR_DOORS_UNLOCKED = "RearDoorsUnlocked"
    REAR_DOORS_LOCKED = "RearDoorsLocked"
    TRUNK_LOCKED = "TrunkLocked"
    TRUNK_UN_LOCKED = "TrunkUnLocked"

    def visit(
        self,
        unlocked: typing.Callable[[], T_Result],
        locked: typing.Callable[[], T_Result],
        super_locked: typing.Callable[[], T_Result],
        driver_door_unlocked: typing.Callable[[], T_Result],
        cabin_doors_unlocked: typing.Callable[[], T_Result],
        cargo_doors_locked: typing.Callable[[], T_Result],
        cargo_doors_unlocked: typing.Callable[[], T_Result],
        rear_doors_unlocked: typing.Callable[[], T_Result],
        rear_doors_locked: typing.Callable[[], T_Result],
        trunk_locked: typing.Callable[[], T_Result],
        trunk_un_locked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DoorsStateBaseLockedStatesItem.UNLOCKED:
            return unlocked()
        if self is DoorsStateBaseLockedStatesItem.LOCKED:
            return locked()
        if self is DoorsStateBaseLockedStatesItem.SUPER_LOCKED:
            return super_locked()
        if self is DoorsStateBaseLockedStatesItem.DRIVER_DOOR_UNLOCKED:
            return driver_door_unlocked()
        if self is DoorsStateBaseLockedStatesItem.CABIN_DOORS_UNLOCKED:
            return cabin_doors_unlocked()
        if self is DoorsStateBaseLockedStatesItem.CARGO_DOORS_LOCKED:
            return cargo_doors_locked()
        if self is DoorsStateBaseLockedStatesItem.CARGO_DOORS_UNLOCKED:
            return cargo_doors_unlocked()
        if self is DoorsStateBaseLockedStatesItem.REAR_DOORS_UNLOCKED:
            return rear_doors_unlocked()
        if self is DoorsStateBaseLockedStatesItem.REAR_DOORS_LOCKED:
            return rear_doors_locked()
        if self is DoorsStateBaseLockedStatesItem.TRUNK_LOCKED:
            return trunk_locked()
        if self is DoorsStateBaseLockedStatesItem.TRUNK_UN_LOCKED:
            return trunk_un_locked()
