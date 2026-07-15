

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiClassesIndexLevelsClassLevelRequestIndex(str, enum.Enum):
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
        if self is GetApiClassesIndexLevelsClassLevelRequestIndex.BARBARIAN:
            return barbarian()
        if self is GetApiClassesIndexLevelsClassLevelRequestIndex.BARD:
            return bard()
        if self is GetApiClassesIndexLevelsClassLevelRequestIndex.CLERIC:
            return cleric()
        if self is GetApiClassesIndexLevelsClassLevelRequestIndex.DRUID:
            return druid()
        if self is GetApiClassesIndexLevelsClassLevelRequestIndex.FIGHTER:
            return fighter()
        if self is GetApiClassesIndexLevelsClassLevelRequestIndex.MONK:
            return monk()
        if self is GetApiClassesIndexLevelsClassLevelRequestIndex.PALADIN:
            return paladin()
        if self is GetApiClassesIndexLevelsClassLevelRequestIndex.RANGER:
            return ranger()
        if self is GetApiClassesIndexLevelsClassLevelRequestIndex.ROGUE:
            return rogue()
        if self is GetApiClassesIndexLevelsClassLevelRequestIndex.SORCERER:
            return sorcerer()
        if self is GetApiClassesIndexLevelsClassLevelRequestIndex.WARLOCK:
            return warlock()
        if self is GetApiClassesIndexLevelsClassLevelRequestIndex.WIZARD:
            return wizard()
