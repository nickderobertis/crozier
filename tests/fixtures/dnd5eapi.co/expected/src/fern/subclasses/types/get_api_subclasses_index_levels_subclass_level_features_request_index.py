

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex(enum.StrEnum):
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
        if self is GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.BERSERKER:
            return berserker()
        if self is GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.CHAMPION:
            return champion()
        if self is GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.DEVOTION:
            return devotion()
        if self is GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.DRACONIC:
            return draconic()
        if self is GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.EVOCATION:
            return evocation()
        if self is GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.FIEND:
            return fiend()
        if self is GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.HUNTER:
            return hunter()
        if self is GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.LAND:
            return land()
        if self is GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.LIFE:
            return life()
        if self is GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.LORE:
            return lore()
        if self is GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.OPEN_HAND:
            return open_hand()
        if self is GetApiSubclassesIndexLevelsSubclassLevelFeaturesRequestIndex.THIEF:
            return thief()
