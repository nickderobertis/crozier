

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex(str, enum.Enum):
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
        if self is GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.BARBARIAN:
            return barbarian()
        if self is GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.BARD:
            return bard()
        if self is GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.CLERIC:
            return cleric()
        if self is GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.DRUID:
            return druid()
        if self is GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.FIGHTER:
            return fighter()
        if self is GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.MONK:
            return monk()
        if self is GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.PALADIN:
            return paladin()
        if self is GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.RANGER:
            return ranger()
        if self is GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.ROGUE:
            return rogue()
        if self is GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.SORCERER:
            return sorcerer()
        if self is GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.WARLOCK:
            return warlock()
        if self is GetApiClassesIndexLevelsClassLevelFeaturesRequestIndex.WIZARD:
            return wizard()
