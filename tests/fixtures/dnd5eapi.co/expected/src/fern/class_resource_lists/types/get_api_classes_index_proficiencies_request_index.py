

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiClassesIndexProficienciesRequestIndex(enum.StrEnum):
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
        if self is GetApiClassesIndexProficienciesRequestIndex.BARBARIAN:
            return barbarian()
        if self is GetApiClassesIndexProficienciesRequestIndex.BARD:
            return bard()
        if self is GetApiClassesIndexProficienciesRequestIndex.CLERIC:
            return cleric()
        if self is GetApiClassesIndexProficienciesRequestIndex.DRUID:
            return druid()
        if self is GetApiClassesIndexProficienciesRequestIndex.FIGHTER:
            return fighter()
        if self is GetApiClassesIndexProficienciesRequestIndex.MONK:
            return monk()
        if self is GetApiClassesIndexProficienciesRequestIndex.PALADIN:
            return paladin()
        if self is GetApiClassesIndexProficienciesRequestIndex.RANGER:
            return ranger()
        if self is GetApiClassesIndexProficienciesRequestIndex.ROGUE:
            return rogue()
        if self is GetApiClassesIndexProficienciesRequestIndex.SORCERER:
            return sorcerer()
        if self is GetApiClassesIndexProficienciesRequestIndex.WARLOCK:
            return warlock()
        if self is GetApiClassesIndexProficienciesRequestIndex.WIZARD:
            return wizard()
