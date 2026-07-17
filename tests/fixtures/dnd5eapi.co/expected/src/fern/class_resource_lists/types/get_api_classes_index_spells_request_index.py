

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiClassesIndexSpellsRequestIndex(enum.StrEnum):
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
        if self is GetApiClassesIndexSpellsRequestIndex.BARBARIAN:
            return barbarian()
        if self is GetApiClassesIndexSpellsRequestIndex.BARD:
            return bard()
        if self is GetApiClassesIndexSpellsRequestIndex.CLERIC:
            return cleric()
        if self is GetApiClassesIndexSpellsRequestIndex.DRUID:
            return druid()
        if self is GetApiClassesIndexSpellsRequestIndex.FIGHTER:
            return fighter()
        if self is GetApiClassesIndexSpellsRequestIndex.MONK:
            return monk()
        if self is GetApiClassesIndexSpellsRequestIndex.PALADIN:
            return paladin()
        if self is GetApiClassesIndexSpellsRequestIndex.RANGER:
            return ranger()
        if self is GetApiClassesIndexSpellsRequestIndex.ROGUE:
            return rogue()
        if self is GetApiClassesIndexSpellsRequestIndex.SORCERER:
            return sorcerer()
        if self is GetApiClassesIndexSpellsRequestIndex.WARLOCK:
            return warlock()
        if self is GetApiClassesIndexSpellsRequestIndex.WIZARD:
            return wizard()
