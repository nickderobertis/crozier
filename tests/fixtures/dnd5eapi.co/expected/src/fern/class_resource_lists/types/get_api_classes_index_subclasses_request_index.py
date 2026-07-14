

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiClassesIndexSubclassesRequestIndex(str, enum.Enum):
    BARBARIAN = "barbarian"
    BARD = "bard"
    CLERIC = "cleric"
    DRUID = "druid"
    FIGHTER = "fighter"
    MONK = "monk"
    PALADIN = "paladin"
    RANGER = "ranger"
    ROGUE = "rogue"
    SORCERER = "sorcerer"
    WARLOCK = "warlock"
    WIZARD = "wizard"

    def visit(
        self,
        barbarian: typing.Callable[[], T_Result],
        bard: typing.Callable[[], T_Result],
        cleric: typing.Callable[[], T_Result],
        druid: typing.Callable[[], T_Result],
        fighter: typing.Callable[[], T_Result],
        monk: typing.Callable[[], T_Result],
        paladin: typing.Callable[[], T_Result],
        ranger: typing.Callable[[], T_Result],
        rogue: typing.Callable[[], T_Result],
        sorcerer: typing.Callable[[], T_Result],
        warlock: typing.Callable[[], T_Result],
        wizard: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiClassesIndexSubclassesRequestIndex.BARBARIAN:
            return barbarian()
        if self is GetApiClassesIndexSubclassesRequestIndex.BARD:
            return bard()
        if self is GetApiClassesIndexSubclassesRequestIndex.CLERIC:
            return cleric()
        if self is GetApiClassesIndexSubclassesRequestIndex.DRUID:
            return druid()
        if self is GetApiClassesIndexSubclassesRequestIndex.FIGHTER:
            return fighter()
        if self is GetApiClassesIndexSubclassesRequestIndex.MONK:
            return monk()
        if self is GetApiClassesIndexSubclassesRequestIndex.PALADIN:
            return paladin()
        if self is GetApiClassesIndexSubclassesRequestIndex.RANGER:
            return ranger()
        if self is GetApiClassesIndexSubclassesRequestIndex.ROGUE:
            return rogue()
        if self is GetApiClassesIndexSubclassesRequestIndex.SORCERER:
            return sorcerer()
        if self is GetApiClassesIndexSubclassesRequestIndex.WARLOCK:
            return warlock()
        if self is GetApiClassesIndexSubclassesRequestIndex.WIZARD:
            return wizard()
