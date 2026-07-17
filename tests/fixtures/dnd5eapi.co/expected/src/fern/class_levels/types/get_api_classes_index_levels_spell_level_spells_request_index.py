

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex(enum.StrEnum):
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
        if self is GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.BARBARIAN:
            return barbarian()
        if self is GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.BARD:
            return bard()
        if self is GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.CLERIC:
            return cleric()
        if self is GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.DRUID:
            return druid()
        if self is GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.FIGHTER:
            return fighter()
        if self is GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.MONK:
            return monk()
        if self is GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.PALADIN:
            return paladin()
        if self is GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.RANGER:
            return ranger()
        if self is GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.ROGUE:
            return rogue()
        if self is GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.SORCERER:
            return sorcerer()
        if self is GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.WARLOCK:
            return warlock()
        if self is GetApiClassesIndexLevelsSpellLevelSpellsRequestIndex.WIZARD:
            return wizard()
