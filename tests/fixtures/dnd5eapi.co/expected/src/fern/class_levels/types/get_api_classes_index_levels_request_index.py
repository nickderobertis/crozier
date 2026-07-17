

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiClassesIndexLevelsRequestIndex(enum.StrEnum):
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
        if self is GetApiClassesIndexLevelsRequestIndex.BARBARIAN:
            return barbarian()
        if self is GetApiClassesIndexLevelsRequestIndex.BARD:
            return bard()
        if self is GetApiClassesIndexLevelsRequestIndex.CLERIC:
            return cleric()
        if self is GetApiClassesIndexLevelsRequestIndex.DRUID:
            return druid()
        if self is GetApiClassesIndexLevelsRequestIndex.FIGHTER:
            return fighter()
        if self is GetApiClassesIndexLevelsRequestIndex.MONK:
            return monk()
        if self is GetApiClassesIndexLevelsRequestIndex.PALADIN:
            return paladin()
        if self is GetApiClassesIndexLevelsRequestIndex.RANGER:
            return ranger()
        if self is GetApiClassesIndexLevelsRequestIndex.ROGUE:
            return rogue()
        if self is GetApiClassesIndexLevelsRequestIndex.SORCERER:
            return sorcerer()
        if self is GetApiClassesIndexLevelsRequestIndex.WARLOCK:
            return warlock()
        if self is GetApiClassesIndexLevelsRequestIndex.WIZARD:
            return wizard()
