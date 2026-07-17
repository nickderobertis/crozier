

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiSubclassesIndexLevelsRequestIndex(enum.StrEnum):
    BERSERKER = "berserker"
    CHAMPION = "champion"
    DEVOTION = "devotion"
    DRACONIC = "draconic"
    EVOCATION = "evocation"
    FIEND = "fiend"
    HUNTER = "hunter"
    LAND = "land"
    LIFE = "life"
    LORE = "lore"
    OPEN_HAND = "open-hand"
    THIEF = "thief"

    def visit(
        self,
        berserker: typing.Callable[[], T_Result],
        champion: typing.Callable[[], T_Result],
        devotion: typing.Callable[[], T_Result],
        draconic: typing.Callable[[], T_Result],
        evocation: typing.Callable[[], T_Result],
        fiend: typing.Callable[[], T_Result],
        hunter: typing.Callable[[], T_Result],
        land: typing.Callable[[], T_Result],
        life: typing.Callable[[], T_Result],
        lore: typing.Callable[[], T_Result],
        open_hand: typing.Callable[[], T_Result],
        thief: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiSubclassesIndexLevelsRequestIndex.BERSERKER:
            return berserker()
        if self is GetApiSubclassesIndexLevelsRequestIndex.CHAMPION:
            return champion()
        if self is GetApiSubclassesIndexLevelsRequestIndex.DEVOTION:
            return devotion()
        if self is GetApiSubclassesIndexLevelsRequestIndex.DRACONIC:
            return draconic()
        if self is GetApiSubclassesIndexLevelsRequestIndex.EVOCATION:
            return evocation()
        if self is GetApiSubclassesIndexLevelsRequestIndex.FIEND:
            return fiend()
        if self is GetApiSubclassesIndexLevelsRequestIndex.HUNTER:
            return hunter()
        if self is GetApiSubclassesIndexLevelsRequestIndex.LAND:
            return land()
        if self is GetApiSubclassesIndexLevelsRequestIndex.LIFE:
            return life()
        if self is GetApiSubclassesIndexLevelsRequestIndex.LORE:
            return lore()
        if self is GetApiSubclassesIndexLevelsRequestIndex.OPEN_HAND:
            return open_hand()
        if self is GetApiSubclassesIndexLevelsRequestIndex.THIEF:
            return thief()
