

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiTraitsIndexRequestIndex(str, enum.Enum):
    ARTIFICERS_LORE = "artificers-lore"
    BRAVE = "brave"
    BREATH_WEAPON = "breath-weapon"
    DAMAGE_RESISTANCE = "damage-resistance"
    DARKVISION = "darkvision"
    DRACONIC_ANCESTRY = "draconic-ancestry"
    DRACONIC_ANCESTRY_BLACK = "draconic-ancestry-black"
    DRACONIC_ANCESTRY_BLUE = "draconic-ancestry-blue"
    DRACONIC_ANCESTRY_BRASS = "draconic-ancestry-brass"
    DRACONIC_ANCESTRY_BRONZE = "draconic-ancestry-bronze"
    DRACONIC_ANCESTRY_COPPER = "draconic-ancestry-copper"
    DRACONIC_ANCESTRY_GOLD = "draconic-ancestry-gold"
    DRACONIC_ANCESTRY_GREEN = "draconic-ancestry-green"
    DRACONIC_ANCESTRY_RED = "draconic-ancestry-red"
    DRACONIC_ANCESTRY_SILVER = "draconic-ancestry-silver"
    DRACONIC_ANCESTRY_WHITE = "draconic-ancestry-white"
    DWARVEN_COMBAT_TRAINING = "dwarven-combat-training"
    DWARVEN_RESILIENCE = "dwarven-resilience"
    DWARVEN_TOUGHNESS = "dwarven-toughness"
    ELF_WEAPON_TRAINING = "elf-weapon-training"
    EXTRA_LANGUAGE = "extra-language"
    FEY_ANCESTRY = "fey-ancestry"
    GNOME_CUNNING = "gnome-cunning"
    HALFLING_NIMBLENESS = "halfling-nimbleness"
    HELLISH_RESISTANCE = "hellish-resistance"
    HIGH_ELF_CANTRIP = "high-elf-cantrip"
    INFERNAL_LEGACY = "infernal-legacy"
    KEEN_SENSES = "keen-senses"
    LUCKY = "lucky"
    MENACING = "menacing"
    NATURALLY_STEALTHY = "naturally-stealthy"
    RELENTLESS_ENDURANCE = "relentless-endurance"
    SAVAGE_ATTACKS = "savage-attacks"
    SKILL_VERSATILITY = "skill-versatility"
    STONECUNNING = "stonecunning"
    TINKER = "tinker"
    TOOL_PROFICIENCY = "tool-proficiency"
    TRANCE = "trance"

    def visit(
        self,
        artificers_lore: typing.Callable[[], T_Result],
        brave: typing.Callable[[], T_Result],
        breath_weapon: typing.Callable[[], T_Result],
        damage_resistance: typing.Callable[[], T_Result],
        darkvision: typing.Callable[[], T_Result],
        draconic_ancestry: typing.Callable[[], T_Result],
        draconic_ancestry_black: typing.Callable[[], T_Result],
        draconic_ancestry_blue: typing.Callable[[], T_Result],
        draconic_ancestry_brass: typing.Callable[[], T_Result],
        draconic_ancestry_bronze: typing.Callable[[], T_Result],
        draconic_ancestry_copper: typing.Callable[[], T_Result],
        draconic_ancestry_gold: typing.Callable[[], T_Result],
        draconic_ancestry_green: typing.Callable[[], T_Result],
        draconic_ancestry_red: typing.Callable[[], T_Result],
        draconic_ancestry_silver: typing.Callable[[], T_Result],
        draconic_ancestry_white: typing.Callable[[], T_Result],
        dwarven_combat_training: typing.Callable[[], T_Result],
        dwarven_resilience: typing.Callable[[], T_Result],
        dwarven_toughness: typing.Callable[[], T_Result],
        elf_weapon_training: typing.Callable[[], T_Result],
        extra_language: typing.Callable[[], T_Result],
        fey_ancestry: typing.Callable[[], T_Result],
        gnome_cunning: typing.Callable[[], T_Result],
        halfling_nimbleness: typing.Callable[[], T_Result],
        hellish_resistance: typing.Callable[[], T_Result],
        high_elf_cantrip: typing.Callable[[], T_Result],
        infernal_legacy: typing.Callable[[], T_Result],
        keen_senses: typing.Callable[[], T_Result],
        lucky: typing.Callable[[], T_Result],
        menacing: typing.Callable[[], T_Result],
        naturally_stealthy: typing.Callable[[], T_Result],
        relentless_endurance: typing.Callable[[], T_Result],
        savage_attacks: typing.Callable[[], T_Result],
        skill_versatility: typing.Callable[[], T_Result],
        stonecunning: typing.Callable[[], T_Result],
        tinker: typing.Callable[[], T_Result],
        tool_proficiency: typing.Callable[[], T_Result],
        trance: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiTraitsIndexRequestIndex.ARTIFICERS_LORE:
            return artificers_lore()
        if self is GetApiTraitsIndexRequestIndex.BRAVE:
            return brave()
        if self is GetApiTraitsIndexRequestIndex.BREATH_WEAPON:
            return breath_weapon()
        if self is GetApiTraitsIndexRequestIndex.DAMAGE_RESISTANCE:
            return damage_resistance()
        if self is GetApiTraitsIndexRequestIndex.DARKVISION:
            return darkvision()
        if self is GetApiTraitsIndexRequestIndex.DRACONIC_ANCESTRY:
            return draconic_ancestry()
        if self is GetApiTraitsIndexRequestIndex.DRACONIC_ANCESTRY_BLACK:
            return draconic_ancestry_black()
        if self is GetApiTraitsIndexRequestIndex.DRACONIC_ANCESTRY_BLUE:
            return draconic_ancestry_blue()
        if self is GetApiTraitsIndexRequestIndex.DRACONIC_ANCESTRY_BRASS:
            return draconic_ancestry_brass()
        if self is GetApiTraitsIndexRequestIndex.DRACONIC_ANCESTRY_BRONZE:
            return draconic_ancestry_bronze()
        if self is GetApiTraitsIndexRequestIndex.DRACONIC_ANCESTRY_COPPER:
            return draconic_ancestry_copper()
        if self is GetApiTraitsIndexRequestIndex.DRACONIC_ANCESTRY_GOLD:
            return draconic_ancestry_gold()
        if self is GetApiTraitsIndexRequestIndex.DRACONIC_ANCESTRY_GREEN:
            return draconic_ancestry_green()
        if self is GetApiTraitsIndexRequestIndex.DRACONIC_ANCESTRY_RED:
            return draconic_ancestry_red()
        if self is GetApiTraitsIndexRequestIndex.DRACONIC_ANCESTRY_SILVER:
            return draconic_ancestry_silver()
        if self is GetApiTraitsIndexRequestIndex.DRACONIC_ANCESTRY_WHITE:
            return draconic_ancestry_white()
        if self is GetApiTraitsIndexRequestIndex.DWARVEN_COMBAT_TRAINING:
            return dwarven_combat_training()
        if self is GetApiTraitsIndexRequestIndex.DWARVEN_RESILIENCE:
            return dwarven_resilience()
        if self is GetApiTraitsIndexRequestIndex.DWARVEN_TOUGHNESS:
            return dwarven_toughness()
        if self is GetApiTraitsIndexRequestIndex.ELF_WEAPON_TRAINING:
            return elf_weapon_training()
        if self is GetApiTraitsIndexRequestIndex.EXTRA_LANGUAGE:
            return extra_language()
        if self is GetApiTraitsIndexRequestIndex.FEY_ANCESTRY:
            return fey_ancestry()
        if self is GetApiTraitsIndexRequestIndex.GNOME_CUNNING:
            return gnome_cunning()
        if self is GetApiTraitsIndexRequestIndex.HALFLING_NIMBLENESS:
            return halfling_nimbleness()
        if self is GetApiTraitsIndexRequestIndex.HELLISH_RESISTANCE:
            return hellish_resistance()
        if self is GetApiTraitsIndexRequestIndex.HIGH_ELF_CANTRIP:
            return high_elf_cantrip()
        if self is GetApiTraitsIndexRequestIndex.INFERNAL_LEGACY:
            return infernal_legacy()
        if self is GetApiTraitsIndexRequestIndex.KEEN_SENSES:
            return keen_senses()
        if self is GetApiTraitsIndexRequestIndex.LUCKY:
            return lucky()
        if self is GetApiTraitsIndexRequestIndex.MENACING:
            return menacing()
        if self is GetApiTraitsIndexRequestIndex.NATURALLY_STEALTHY:
            return naturally_stealthy()
        if self is GetApiTraitsIndexRequestIndex.RELENTLESS_ENDURANCE:
            return relentless_endurance()
        if self is GetApiTraitsIndexRequestIndex.SAVAGE_ATTACKS:
            return savage_attacks()
        if self is GetApiTraitsIndexRequestIndex.SKILL_VERSATILITY:
            return skill_versatility()
        if self is GetApiTraitsIndexRequestIndex.STONECUNNING:
            return stonecunning()
        if self is GetApiTraitsIndexRequestIndex.TINKER:
            return tinker()
        if self is GetApiTraitsIndexRequestIndex.TOOL_PROFICIENCY:
            return tool_proficiency()
        if self is GetApiTraitsIndexRequestIndex.TRANCE:
            return trance()
