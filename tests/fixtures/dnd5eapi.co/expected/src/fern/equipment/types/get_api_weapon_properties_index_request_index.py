

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiWeaponPropertiesIndexRequestIndex(enum.StrEnum):
    AMMUNITION = "ammunition"
    FINESSE = "finesse"
    HEAVY = "heavy"
    LIGHT = "light"
    LOADING = "loading"
    MONK = "monk"
    REACH = "reach"
    SPECIAL = "special"
    THROWN = "thrown"
    TWO_HANDED = "two-handed"
    VERSATILE = "versatile"

    def visit(
        self,
        ammunition: typing.Callable[[], T_Result],
        finesse: typing.Callable[[], T_Result],
        heavy: typing.Callable[[], T_Result],
        light: typing.Callable[[], T_Result],
        loading: typing.Callable[[], T_Result],
        monk: typing.Callable[[], T_Result],
        reach: typing.Callable[[], T_Result],
        special: typing.Callable[[], T_Result],
        thrown: typing.Callable[[], T_Result],
        two_handed: typing.Callable[[], T_Result],
        versatile: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiWeaponPropertiesIndexRequestIndex.AMMUNITION:
            return ammunition()
        if self is GetApiWeaponPropertiesIndexRequestIndex.FINESSE:
            return finesse()
        if self is GetApiWeaponPropertiesIndexRequestIndex.HEAVY:
            return heavy()
        if self is GetApiWeaponPropertiesIndexRequestIndex.LIGHT:
            return light()
        if self is GetApiWeaponPropertiesIndexRequestIndex.LOADING:
            return loading()
        if self is GetApiWeaponPropertiesIndexRequestIndex.MONK:
            return monk()
        if self is GetApiWeaponPropertiesIndexRequestIndex.REACH:
            return reach()
        if self is GetApiWeaponPropertiesIndexRequestIndex.SPECIAL:
            return special()
        if self is GetApiWeaponPropertiesIndexRequestIndex.THROWN:
            return thrown()
        if self is GetApiWeaponPropertiesIndexRequestIndex.TWO_HANDED:
            return two_handed()
        if self is GetApiWeaponPropertiesIndexRequestIndex.VERSATILE:
            return versatile()
