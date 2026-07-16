

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiClassesIndexMultiClassingRequestIndex(enum.StrEnum):
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
        if self is GetApiClassesIndexMultiClassingRequestIndex.BARBARIAN:
            return barbarian()
        if self is GetApiClassesIndexMultiClassingRequestIndex.BARD:
            return bard()
        if self is GetApiClassesIndexMultiClassingRequestIndex.CLERIC:
            return cleric()
        if self is GetApiClassesIndexMultiClassingRequestIndex.DRUID:
            return druid()
        if self is GetApiClassesIndexMultiClassingRequestIndex.FIGHTER:
            return fighter()
        if self is GetApiClassesIndexMultiClassingRequestIndex.MONK:
            return monk()
        if self is GetApiClassesIndexMultiClassingRequestIndex.PALADIN:
            return paladin()
        if self is GetApiClassesIndexMultiClassingRequestIndex.RANGER:
            return ranger()
        if self is GetApiClassesIndexMultiClassingRequestIndex.ROGUE:
            return rogue()
        if self is GetApiClassesIndexMultiClassingRequestIndex.SORCERER:
            return sorcerer()
        if self is GetApiClassesIndexMultiClassingRequestIndex.WARLOCK:
            return warlock()
        if self is GetApiClassesIndexMultiClassingRequestIndex.WIZARD:
            return wizard()
