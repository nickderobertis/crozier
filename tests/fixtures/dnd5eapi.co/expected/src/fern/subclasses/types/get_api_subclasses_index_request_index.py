

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiSubclassesIndexRequestIndex(str, enum.Enum):
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
        if self is GetApiSubclassesIndexRequestIndex.BERSERKER:
            return berserker()
        if self is GetApiSubclassesIndexRequestIndex.CHAMPION:
            return champion()
        if self is GetApiSubclassesIndexRequestIndex.DEVOTION:
            return devotion()
        if self is GetApiSubclassesIndexRequestIndex.DRACONIC:
            return draconic()
        if self is GetApiSubclassesIndexRequestIndex.EVOCATION:
            return evocation()
        if self is GetApiSubclassesIndexRequestIndex.FIEND:
            return fiend()
        if self is GetApiSubclassesIndexRequestIndex.HUNTER:
            return hunter()
        if self is GetApiSubclassesIndexRequestIndex.LAND:
            return land()
        if self is GetApiSubclassesIndexRequestIndex.LIFE:
            return life()
        if self is GetApiSubclassesIndexRequestIndex.LORE:
            return lore()
        if self is GetApiSubclassesIndexRequestIndex.OPEN_HAND:
            return open_hand()
        if self is GetApiSubclassesIndexRequestIndex.THIEF:
            return thief()
