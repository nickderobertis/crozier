

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiClassesIndexFeaturesRequestIndex(str, enum.Enum):
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
        if self is GetApiClassesIndexFeaturesRequestIndex.BARBARIAN:
            return barbarian()
        if self is GetApiClassesIndexFeaturesRequestIndex.BARD:
            return bard()
        if self is GetApiClassesIndexFeaturesRequestIndex.CLERIC:
            return cleric()
        if self is GetApiClassesIndexFeaturesRequestIndex.DRUID:
            return druid()
        if self is GetApiClassesIndexFeaturesRequestIndex.FIGHTER:
            return fighter()
        if self is GetApiClassesIndexFeaturesRequestIndex.MONK:
            return monk()
        if self is GetApiClassesIndexFeaturesRequestIndex.PALADIN:
            return paladin()
        if self is GetApiClassesIndexFeaturesRequestIndex.RANGER:
            return ranger()
        if self is GetApiClassesIndexFeaturesRequestIndex.ROGUE:
            return rogue()
        if self is GetApiClassesIndexFeaturesRequestIndex.SORCERER:
            return sorcerer()
        if self is GetApiClassesIndexFeaturesRequestIndex.WARLOCK:
            return warlock()
        if self is GetApiClassesIndexFeaturesRequestIndex.WIZARD:
            return wizard()
