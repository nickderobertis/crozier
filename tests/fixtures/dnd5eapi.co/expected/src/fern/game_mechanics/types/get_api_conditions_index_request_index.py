

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiConditionsIndexRequestIndex(enum.StrEnum):
    BLINDED = "blinded"
    CHARMED = "charmed"
    DEAFENED = "deafened"
    EXHAUSTION = "exhaustion"
    FRIGHTENED = "frightened"
    GRAPPLED = "grappled"
    INCAPACITATED = "incapacitated"
    INVISIBLE = "invisible"
    PARALYZED = "paralyzed"
    PETRIFIED = "petrified"
    POISONED = "poisoned"
    PRONE = "prone"
    RESTRAINED = "restrained"
    STUNNED = "stunned"
    UNCONSCIOUS = "unconscious"

    def visit(
        self,
        blinded: typing.Callable[[], T_Result],
        charmed: typing.Callable[[], T_Result],
        deafened: typing.Callable[[], T_Result],
        exhaustion: typing.Callable[[], T_Result],
        frightened: typing.Callable[[], T_Result],
        grappled: typing.Callable[[], T_Result],
        incapacitated: typing.Callable[[], T_Result],
        invisible: typing.Callable[[], T_Result],
        paralyzed: typing.Callable[[], T_Result],
        petrified: typing.Callable[[], T_Result],
        poisoned: typing.Callable[[], T_Result],
        prone: typing.Callable[[], T_Result],
        restrained: typing.Callable[[], T_Result],
        stunned: typing.Callable[[], T_Result],
        unconscious: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiConditionsIndexRequestIndex.BLINDED:
            return blinded()
        if self is GetApiConditionsIndexRequestIndex.CHARMED:
            return charmed()
        if self is GetApiConditionsIndexRequestIndex.DEAFENED:
            return deafened()
        if self is GetApiConditionsIndexRequestIndex.EXHAUSTION:
            return exhaustion()
        if self is GetApiConditionsIndexRequestIndex.FRIGHTENED:
            return frightened()
        if self is GetApiConditionsIndexRequestIndex.GRAPPLED:
            return grappled()
        if self is GetApiConditionsIndexRequestIndex.INCAPACITATED:
            return incapacitated()
        if self is GetApiConditionsIndexRequestIndex.INVISIBLE:
            return invisible()
        if self is GetApiConditionsIndexRequestIndex.PARALYZED:
            return paralyzed()
        if self is GetApiConditionsIndexRequestIndex.PETRIFIED:
            return petrified()
        if self is GetApiConditionsIndexRequestIndex.POISONED:
            return poisoned()
        if self is GetApiConditionsIndexRequestIndex.PRONE:
            return prone()
        if self is GetApiConditionsIndexRequestIndex.RESTRAINED:
            return restrained()
        if self is GetApiConditionsIndexRequestIndex.STUNNED:
            return stunned()
        if self is GetApiConditionsIndexRequestIndex.UNCONSCIOUS:
            return unconscious()
