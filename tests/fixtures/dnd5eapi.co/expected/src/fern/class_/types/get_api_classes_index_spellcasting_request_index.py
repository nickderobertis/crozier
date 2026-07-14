

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiClassesIndexSpellcastingRequestIndex(str, enum.Enum):
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
        if self is GetApiClassesIndexSpellcastingRequestIndex.BARBARIAN:
            return barbarian()
        if self is GetApiClassesIndexSpellcastingRequestIndex.BARD:
            return bard()
        if self is GetApiClassesIndexSpellcastingRequestIndex.CLERIC:
            return cleric()
        if self is GetApiClassesIndexSpellcastingRequestIndex.DRUID:
            return druid()
        if self is GetApiClassesIndexSpellcastingRequestIndex.FIGHTER:
            return fighter()
        if self is GetApiClassesIndexSpellcastingRequestIndex.MONK:
            return monk()
        if self is GetApiClassesIndexSpellcastingRequestIndex.PALADIN:
            return paladin()
        if self is GetApiClassesIndexSpellcastingRequestIndex.RANGER:
            return ranger()
        if self is GetApiClassesIndexSpellcastingRequestIndex.ROGUE:
            return rogue()
        if self is GetApiClassesIndexSpellcastingRequestIndex.SORCERER:
            return sorcerer()
        if self is GetApiClassesIndexSpellcastingRequestIndex.WARLOCK:
            return warlock()
        if self is GetApiClassesIndexSpellcastingRequestIndex.WIZARD:
            return wizard()
