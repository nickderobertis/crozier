

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiClassesIndexRequestIndex(str, enum.Enum):
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
        if self is GetApiClassesIndexRequestIndex.BARBARIAN:
            return barbarian()
        if self is GetApiClassesIndexRequestIndex.BARD:
            return bard()
        if self is GetApiClassesIndexRequestIndex.CLERIC:
            return cleric()
        if self is GetApiClassesIndexRequestIndex.DRUID:
            return druid()
        if self is GetApiClassesIndexRequestIndex.FIGHTER:
            return fighter()
        if self is GetApiClassesIndexRequestIndex.MONK:
            return monk()
        if self is GetApiClassesIndexRequestIndex.PALADIN:
            return paladin()
        if self is GetApiClassesIndexRequestIndex.RANGER:
            return ranger()
        if self is GetApiClassesIndexRequestIndex.ROGUE:
            return rogue()
        if self is GetApiClassesIndexRequestIndex.SORCERER:
            return sorcerer()
        if self is GetApiClassesIndexRequestIndex.WARLOCK:
            return warlock()
        if self is GetApiClassesIndexRequestIndex.WIZARD:
            return wizard()
