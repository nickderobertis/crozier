

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiDamageTypesIndexRequestIndex(enum.StrEnum):
    ACID = "acid"
    BLUDGEONING = "bludgeoning"
    COLD = "cold"
    FIRE = "fire"
    FORCE = "force"
    LIGHTNING = "lightning"
    NECROTIC = "necrotic"
    PIERCING = "piercing"
    POISON = "poison"
    PSYCHIC = "psychic"
    RADIANT = "radiant"
    SLASHING = "slashing"
    THUNDER = "thunder"

    def visit(
        self,
        acid: typing.Callable[[], T_Result],
        bludgeoning: typing.Callable[[], T_Result],
        cold: typing.Callable[[], T_Result],
        fire: typing.Callable[[], T_Result],
        force: typing.Callable[[], T_Result],
        lightning: typing.Callable[[], T_Result],
        necrotic: typing.Callable[[], T_Result],
        piercing: typing.Callable[[], T_Result],
        poison: typing.Callable[[], T_Result],
        psychic: typing.Callable[[], T_Result],
        radiant: typing.Callable[[], T_Result],
        slashing: typing.Callable[[], T_Result],
        thunder: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiDamageTypesIndexRequestIndex.ACID:
            return acid()
        if self is GetApiDamageTypesIndexRequestIndex.BLUDGEONING:
            return bludgeoning()
        if self is GetApiDamageTypesIndexRequestIndex.COLD:
            return cold()
        if self is GetApiDamageTypesIndexRequestIndex.FIRE:
            return fire()
        if self is GetApiDamageTypesIndexRequestIndex.FORCE:
            return force()
        if self is GetApiDamageTypesIndexRequestIndex.LIGHTNING:
            return lightning()
        if self is GetApiDamageTypesIndexRequestIndex.NECROTIC:
            return necrotic()
        if self is GetApiDamageTypesIndexRequestIndex.PIERCING:
            return piercing()
        if self is GetApiDamageTypesIndexRequestIndex.POISON:
            return poison()
        if self is GetApiDamageTypesIndexRequestIndex.PSYCHIC:
            return psychic()
        if self is GetApiDamageTypesIndexRequestIndex.RADIANT:
            return radiant()
        if self is GetApiDamageTypesIndexRequestIndex.SLASHING:
            return slashing()
        if self is GetApiDamageTypesIndexRequestIndex.THUNDER:
            return thunder()
