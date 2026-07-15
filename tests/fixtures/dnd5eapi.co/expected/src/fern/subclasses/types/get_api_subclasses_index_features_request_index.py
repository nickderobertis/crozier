

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiSubclassesIndexFeaturesRequestIndex(str, enum.Enum):
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
        if self is GetApiSubclassesIndexFeaturesRequestIndex.BERSERKER:
            return berserker()
        if self is GetApiSubclassesIndexFeaturesRequestIndex.CHAMPION:
            return champion()
        if self is GetApiSubclassesIndexFeaturesRequestIndex.DEVOTION:
            return devotion()
        if self is GetApiSubclassesIndexFeaturesRequestIndex.DRACONIC:
            return draconic()
        if self is GetApiSubclassesIndexFeaturesRequestIndex.EVOCATION:
            return evocation()
        if self is GetApiSubclassesIndexFeaturesRequestIndex.FIEND:
            return fiend()
        if self is GetApiSubclassesIndexFeaturesRequestIndex.HUNTER:
            return hunter()
        if self is GetApiSubclassesIndexFeaturesRequestIndex.LAND:
            return land()
        if self is GetApiSubclassesIndexFeaturesRequestIndex.LIFE:
            return life()
        if self is GetApiSubclassesIndexFeaturesRequestIndex.LORE:
            return lore()
        if self is GetApiSubclassesIndexFeaturesRequestIndex.OPEN_HAND:
            return open_hand()
        if self is GetApiSubclassesIndexFeaturesRequestIndex.THIEF:
            return thief()
