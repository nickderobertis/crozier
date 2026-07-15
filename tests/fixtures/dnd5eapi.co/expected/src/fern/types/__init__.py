



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .ability_bonus import AbilityBonus
    from .ability_score import AbilityScore
    from .alignment import Alignment
    from .api_reference import ApiReference
    from .api_reference_list import ApiReferenceList
    from .area_of_effect import AreaOfEffect
    from .area_of_effect_type import AreaOfEffectType
    from .armor import Armor
    from .background import Background
    from .background_feature import BackgroundFeature
    from .choice import Choice
    from .class_ import Class
    from .class_level import ClassLevel
    from .class_level_class_specific import ClassLevelClassSpecific
    from .class_level_class_specific_action_surges import ClassLevelClassSpecificActionSurges
    from .class_level_class_specific_arcane_recover_levels import ClassLevelClassSpecificArcaneRecoverLevels
    from .class_level_class_specific_aura_range import ClassLevelClassSpecificAuraRange
    from .class_level_class_specific_bardic_inspiration_dice import ClassLevelClassSpecificBardicInspirationDice
    from .class_level_class_specific_brutal_critical_dice import ClassLevelClassSpecificBrutalCriticalDice
    from .class_level_class_specific_channel_divinity_charges import ClassLevelClassSpecificChannelDivinityCharges
    from .class_level_class_specific_creating_spell_slots import ClassLevelClassSpecificCreatingSpellSlots
    from .class_level_class_specific_creating_spell_slots_creating_spell_slots_item import (
        ClassLevelClassSpecificCreatingSpellSlotsCreatingSpellSlotsItem,
    )
    from .class_level_class_specific_favored_enemies import ClassLevelClassSpecificFavoredEnemies
    from .class_level_class_specific_invocations_known import ClassLevelClassSpecificInvocationsKnown
    from .class_level_class_specific_ki_points import ClassLevelClassSpecificKiPoints
    from .class_level_class_specific_ki_points_martial_arts import ClassLevelClassSpecificKiPointsMartialArts
    from .class_level_class_specific_sneak_attack import ClassLevelClassSpecificSneakAttack
    from .class_level_class_specific_sneak_attack_sneak_attack import ClassLevelClassSpecificSneakAttackSneakAttack
    from .class_level_class_specific_wild_shape_fly import ClassLevelClassSpecificWildShapeFly
    from .class_level_spellcasting import ClassLevelSpellcasting
    from .class_starting_equipment_item import ClassStartingEquipmentItem
    from .condition import Condition
    from .cost import Cost
    from .damage import Damage
    from .damage_at_character_level import DamageAtCharacterLevel
    from .damage_at_slot_level import DamageAtSlotLevel
    from .damage_type import DamageType
    from .dc import Dc
    from .equipment import Equipment
    from .equipment_category import EquipmentCategory
    from .equipment_pack import EquipmentPack
    from .error_response import ErrorResponse
    from .feat import Feat
    from .feature import Feature
    from .feature_prerequisites_item import FeaturePrerequisitesItem
    from .feature_prerequisites_item_feature import FeaturePrerequisitesItemFeature
    from .feature_prerequisites_item_level import FeaturePrerequisitesItemLevel
    from .feature_prerequisites_item_spell import FeaturePrerequisitesItemSpell
    from .gear import Gear
    from .language import Language
    from .language_type import LanguageType
    from .magic_item import MagicItem
    from .magic_item_rarity import MagicItemRarity
    from .magic_item_rarity_name import MagicItemRarityName
    from .magic_school import MagicSchool
    from .monster import Monster
    from .monster_actions_item import MonsterActionsItem
    from .monster_actions_item_actions_item import MonsterActionsItemActionsItem
    from .monster_actions_item_actions_item_type import MonsterActionsItemActionsItemType
    from .monster_actions_item_attacks_item import MonsterActionsItemAttacksItem
    from .monster_actions_item_damage_item import MonsterActionsItemDamageItem
    from .monster_alignments import MonsterAlignments
    from .monster_armor_class_item import (
        MonsterArmorClassItem,
        MonsterArmorClassItem_Armor,
        MonsterArmorClassItem_Condition,
        MonsterArmorClassItem_Dex,
        MonsterArmorClassItem_Natural,
        MonsterArmorClassItem_Spell,
    )
    from .monster_armor_class_item_armor import MonsterArmorClassItemArmor
    from .monster_armor_class_item_condition import MonsterArmorClassItemCondition
    from .monster_armor_class_item_dex import MonsterArmorClassItemDex
    from .monster_armor_class_item_natural import MonsterArmorClassItemNatural
    from .monster_armor_class_item_spell import MonsterArmorClassItemSpell
    from .monster_legendary_actions_item import MonsterLegendaryActionsItem
    from .monster_legendary_actions_item_actions_item import MonsterLegendaryActionsItemActionsItem
    from .monster_legendary_actions_item_actions_item_type import MonsterLegendaryActionsItemActionsItemType
    from .monster_legendary_actions_item_attacks_item import MonsterLegendaryActionsItemAttacksItem
    from .monster_legendary_actions_item_damage_item import MonsterLegendaryActionsItemDamageItem
    from .monster_proficiencies_item import MonsterProficienciesItem
    from .monster_reactions_item import MonsterReactionsItem
    from .monster_reactions_item_actions_item import MonsterReactionsItemActionsItem
    from .monster_reactions_item_actions_item_type import MonsterReactionsItemActionsItemType
    from .monster_reactions_item_attacks_item import MonsterReactionsItemAttacksItem
    from .monster_reactions_item_damage_item import MonsterReactionsItemDamageItem
    from .monster_senses import MonsterSenses
    from .monster_size import MonsterSize
    from .monster_special_abilities_item import MonsterSpecialAbilitiesItem
    from .monster_special_abilities_item_spellcasting import MonsterSpecialAbilitiesItemSpellcasting
    from .monster_special_abilities_item_spellcasting_spells_item import (
        MonsterSpecialAbilitiesItemSpellcastingSpellsItem,
    )
    from .monster_special_abilities_item_usage import MonsterSpecialAbilitiesItemUsage
    from .monster_special_abilities_item_usage_type import MonsterSpecialAbilitiesItemUsageType
    from .monster_speed import MonsterSpeed
    from .multiclassing import Multiclassing
    from .option import Option
    from .option_action_name import OptionActionName
    from .option_action_name_type import OptionActionNameType
    from .option_alignments import OptionAlignments
    from .option_bonus import OptionBonus
    from .option_choice import OptionChoice
    from .option_damage import OptionDamage
    from .option_damage_dice import OptionDamageDice
    from .option_item import OptionItem
    from .option_items import OptionItems
    from .option_minimum_score import OptionMinimumScore
    from .option_of import OptionOf
    from .option_set import OptionSet
    from .option_set_equipment_category import OptionSetEquipmentCategory
    from .option_set_option_set_type import OptionSetOptionSetType
    from .option_set_options_array import OptionSetOptionsArray
    from .option_string import OptionString
    from .prerequisite import Prerequisite
    from .proficiency import Proficiency
    from .race import Race
    from .resource_description import ResourceDescription
    from .rule import Rule
    from .rule_section import RuleSection
    from .skill import Skill
    from .spell import Spell
    from .spell_components_item import SpellComponentsItem
    from .spell_damage import SpellDamage
    from .spell_prerequisite import SpellPrerequisite
    from .spellcasting import Spellcasting
    from .spellcasting_info_item import SpellcastingInfoItem
    from .subclass import Subclass
    from .subclass_level import SubclassLevel
    from .subclass_level_resource import SubclassLevelResource
    from .subclass_level_spellcasting import SubclassLevelSpellcasting
    from .subclass_spells_item import SubclassSpellsItem
    from .subrace import Subrace
    from .trait import Trait
    from .trait_trait_specific import TraitTraitSpecific
    from .trait_trait_specific_breath_weapon import TraitTraitSpecificBreathWeapon
    from .trait_trait_specific_breath_weapon_breath_weapon import TraitTraitSpecificBreathWeaponBreathWeapon
    from .trait_trait_specific_breath_weapon_breath_weapon_damage import (
        TraitTraitSpecificBreathWeaponBreathWeaponDamage,
    )
    from .trait_trait_specific_breath_weapon_breath_weapon_usage import TraitTraitSpecificBreathWeaponBreathWeaponUsage
    from .weapon import Weapon
    from .weapon_property import WeaponProperty
    from .weapon_range import WeaponRange
_dynamic_imports: typing.Dict[str, str] = {
    "AbilityBonus": ".ability_bonus",
    "AbilityScore": ".ability_score",
    "Alignment": ".alignment",
    "ApiReference": ".api_reference",
    "ApiReferenceList": ".api_reference_list",
    "AreaOfEffect": ".area_of_effect",
    "AreaOfEffectType": ".area_of_effect_type",
    "Armor": ".armor",
    "Background": ".background",
    "BackgroundFeature": ".background_feature",
    "Choice": ".choice",
    "Class": ".class_",
    "ClassLevel": ".class_level",
    "ClassLevelClassSpecific": ".class_level_class_specific",
    "ClassLevelClassSpecificActionSurges": ".class_level_class_specific_action_surges",
    "ClassLevelClassSpecificArcaneRecoverLevels": ".class_level_class_specific_arcane_recover_levels",
    "ClassLevelClassSpecificAuraRange": ".class_level_class_specific_aura_range",
    "ClassLevelClassSpecificBardicInspirationDice": ".class_level_class_specific_bardic_inspiration_dice",
    "ClassLevelClassSpecificBrutalCriticalDice": ".class_level_class_specific_brutal_critical_dice",
    "ClassLevelClassSpecificChannelDivinityCharges": ".class_level_class_specific_channel_divinity_charges",
    "ClassLevelClassSpecificCreatingSpellSlots": ".class_level_class_specific_creating_spell_slots",
    "ClassLevelClassSpecificCreatingSpellSlotsCreatingSpellSlotsItem": ".class_level_class_specific_creating_spell_slots_creating_spell_slots_item",
    "ClassLevelClassSpecificFavoredEnemies": ".class_level_class_specific_favored_enemies",
    "ClassLevelClassSpecificInvocationsKnown": ".class_level_class_specific_invocations_known",
    "ClassLevelClassSpecificKiPoints": ".class_level_class_specific_ki_points",
    "ClassLevelClassSpecificKiPointsMartialArts": ".class_level_class_specific_ki_points_martial_arts",
    "ClassLevelClassSpecificSneakAttack": ".class_level_class_specific_sneak_attack",
    "ClassLevelClassSpecificSneakAttackSneakAttack": ".class_level_class_specific_sneak_attack_sneak_attack",
    "ClassLevelClassSpecificWildShapeFly": ".class_level_class_specific_wild_shape_fly",
    "ClassLevelSpellcasting": ".class_level_spellcasting",
    "ClassStartingEquipmentItem": ".class_starting_equipment_item",
    "Condition": ".condition",
    "Cost": ".cost",
    "Damage": ".damage",
    "DamageAtCharacterLevel": ".damage_at_character_level",
    "DamageAtSlotLevel": ".damage_at_slot_level",
    "DamageType": ".damage_type",
    "Dc": ".dc",
    "Equipment": ".equipment",
    "EquipmentCategory": ".equipment_category",
    "EquipmentPack": ".equipment_pack",
    "ErrorResponse": ".error_response",
    "Feat": ".feat",
    "Feature": ".feature",
    "FeaturePrerequisitesItem": ".feature_prerequisites_item",
    "FeaturePrerequisitesItemFeature": ".feature_prerequisites_item_feature",
    "FeaturePrerequisitesItemLevel": ".feature_prerequisites_item_level",
    "FeaturePrerequisitesItemSpell": ".feature_prerequisites_item_spell",
    "Gear": ".gear",
    "Language": ".language",
    "LanguageType": ".language_type",
    "MagicItem": ".magic_item",
    "MagicItemRarity": ".magic_item_rarity",
    "MagicItemRarityName": ".magic_item_rarity_name",
    "MagicSchool": ".magic_school",
    "Monster": ".monster",
    "MonsterActionsItem": ".monster_actions_item",
    "MonsterActionsItemActionsItem": ".monster_actions_item_actions_item",
    "MonsterActionsItemActionsItemType": ".monster_actions_item_actions_item_type",
    "MonsterActionsItemAttacksItem": ".monster_actions_item_attacks_item",
    "MonsterActionsItemDamageItem": ".monster_actions_item_damage_item",
    "MonsterAlignments": ".monster_alignments",
    "MonsterArmorClassItem": ".monster_armor_class_item",
    "MonsterArmorClassItemArmor": ".monster_armor_class_item_armor",
    "MonsterArmorClassItemCondition": ".monster_armor_class_item_condition",
    "MonsterArmorClassItemDex": ".monster_armor_class_item_dex",
    "MonsterArmorClassItemNatural": ".monster_armor_class_item_natural",
    "MonsterArmorClassItemSpell": ".monster_armor_class_item_spell",
    "MonsterArmorClassItem_Armor": ".monster_armor_class_item",
    "MonsterArmorClassItem_Condition": ".monster_armor_class_item",
    "MonsterArmorClassItem_Dex": ".monster_armor_class_item",
    "MonsterArmorClassItem_Natural": ".monster_armor_class_item",
    "MonsterArmorClassItem_Spell": ".monster_armor_class_item",
    "MonsterLegendaryActionsItem": ".monster_legendary_actions_item",
    "MonsterLegendaryActionsItemActionsItem": ".monster_legendary_actions_item_actions_item",
    "MonsterLegendaryActionsItemActionsItemType": ".monster_legendary_actions_item_actions_item_type",
    "MonsterLegendaryActionsItemAttacksItem": ".monster_legendary_actions_item_attacks_item",
    "MonsterLegendaryActionsItemDamageItem": ".monster_legendary_actions_item_damage_item",
    "MonsterProficienciesItem": ".monster_proficiencies_item",
    "MonsterReactionsItem": ".monster_reactions_item",
    "MonsterReactionsItemActionsItem": ".monster_reactions_item_actions_item",
    "MonsterReactionsItemActionsItemType": ".monster_reactions_item_actions_item_type",
    "MonsterReactionsItemAttacksItem": ".monster_reactions_item_attacks_item",
    "MonsterReactionsItemDamageItem": ".monster_reactions_item_damage_item",
    "MonsterSenses": ".monster_senses",
    "MonsterSize": ".monster_size",
    "MonsterSpecialAbilitiesItem": ".monster_special_abilities_item",
    "MonsterSpecialAbilitiesItemSpellcasting": ".monster_special_abilities_item_spellcasting",
    "MonsterSpecialAbilitiesItemSpellcastingSpellsItem": ".monster_special_abilities_item_spellcasting_spells_item",
    "MonsterSpecialAbilitiesItemUsage": ".monster_special_abilities_item_usage",
    "MonsterSpecialAbilitiesItemUsageType": ".monster_special_abilities_item_usage_type",
    "MonsterSpeed": ".monster_speed",
    "Multiclassing": ".multiclassing",
    "Option": ".option",
    "OptionActionName": ".option_action_name",
    "OptionActionNameType": ".option_action_name_type",
    "OptionAlignments": ".option_alignments",
    "OptionBonus": ".option_bonus",
    "OptionChoice": ".option_choice",
    "OptionDamage": ".option_damage",
    "OptionDamageDice": ".option_damage_dice",
    "OptionItem": ".option_item",
    "OptionItems": ".option_items",
    "OptionMinimumScore": ".option_minimum_score",
    "OptionOf": ".option_of",
    "OptionSet": ".option_set",
    "OptionSetEquipmentCategory": ".option_set_equipment_category",
    "OptionSetOptionSetType": ".option_set_option_set_type",
    "OptionSetOptionsArray": ".option_set_options_array",
    "OptionString": ".option_string",
    "Prerequisite": ".prerequisite",
    "Proficiency": ".proficiency",
    "Race": ".race",
    "ResourceDescription": ".resource_description",
    "Rule": ".rule",
    "RuleSection": ".rule_section",
    "Skill": ".skill",
    "Spell": ".spell",
    "SpellComponentsItem": ".spell_components_item",
    "SpellDamage": ".spell_damage",
    "SpellPrerequisite": ".spell_prerequisite",
    "Spellcasting": ".spellcasting",
    "SpellcastingInfoItem": ".spellcasting_info_item",
    "Subclass": ".subclass",
    "SubclassLevel": ".subclass_level",
    "SubclassLevelResource": ".subclass_level_resource",
    "SubclassLevelSpellcasting": ".subclass_level_spellcasting",
    "SubclassSpellsItem": ".subclass_spells_item",
    "Subrace": ".subrace",
    "Trait": ".trait",
    "TraitTraitSpecific": ".trait_trait_specific",
    "TraitTraitSpecificBreathWeapon": ".trait_trait_specific_breath_weapon",
    "TraitTraitSpecificBreathWeaponBreathWeapon": ".trait_trait_specific_breath_weapon_breath_weapon",
    "TraitTraitSpecificBreathWeaponBreathWeaponDamage": ".trait_trait_specific_breath_weapon_breath_weapon_damage",
    "TraitTraitSpecificBreathWeaponBreathWeaponUsage": ".trait_trait_specific_breath_weapon_breath_weapon_usage",
    "Weapon": ".weapon",
    "WeaponProperty": ".weapon_property",
    "WeaponRange": ".weapon_range",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AbilityBonus",
    "AbilityScore",
    "Alignment",
    "ApiReference",
    "ApiReferenceList",
    "AreaOfEffect",
    "AreaOfEffectType",
    "Armor",
    "Background",
    "BackgroundFeature",
    "Choice",
    "Class",
    "ClassLevel",
    "ClassLevelClassSpecific",
    "ClassLevelClassSpecificActionSurges",
    "ClassLevelClassSpecificArcaneRecoverLevels",
    "ClassLevelClassSpecificAuraRange",
    "ClassLevelClassSpecificBardicInspirationDice",
    "ClassLevelClassSpecificBrutalCriticalDice",
    "ClassLevelClassSpecificChannelDivinityCharges",
    "ClassLevelClassSpecificCreatingSpellSlots",
    "ClassLevelClassSpecificCreatingSpellSlotsCreatingSpellSlotsItem",
    "ClassLevelClassSpecificFavoredEnemies",
    "ClassLevelClassSpecificInvocationsKnown",
    "ClassLevelClassSpecificKiPoints",
    "ClassLevelClassSpecificKiPointsMartialArts",
    "ClassLevelClassSpecificSneakAttack",
    "ClassLevelClassSpecificSneakAttackSneakAttack",
    "ClassLevelClassSpecificWildShapeFly",
    "ClassLevelSpellcasting",
    "ClassStartingEquipmentItem",
    "Condition",
    "Cost",
    "Damage",
    "DamageAtCharacterLevel",
    "DamageAtSlotLevel",
    "DamageType",
    "Dc",
    "Equipment",
    "EquipmentCategory",
    "EquipmentPack",
    "ErrorResponse",
    "Feat",
    "Feature",
    "FeaturePrerequisitesItem",
    "FeaturePrerequisitesItemFeature",
    "FeaturePrerequisitesItemLevel",
    "FeaturePrerequisitesItemSpell",
    "Gear",
    "Language",
    "LanguageType",
    "MagicItem",
    "MagicItemRarity",
    "MagicItemRarityName",
    "MagicSchool",
    "Monster",
    "MonsterActionsItem",
    "MonsterActionsItemActionsItem",
    "MonsterActionsItemActionsItemType",
    "MonsterActionsItemAttacksItem",
    "MonsterActionsItemDamageItem",
    "MonsterAlignments",
    "MonsterArmorClassItem",
    "MonsterArmorClassItemArmor",
    "MonsterArmorClassItemCondition",
    "MonsterArmorClassItemDex",
    "MonsterArmorClassItemNatural",
    "MonsterArmorClassItemSpell",
    "MonsterArmorClassItem_Armor",
    "MonsterArmorClassItem_Condition",
    "MonsterArmorClassItem_Dex",
    "MonsterArmorClassItem_Natural",
    "MonsterArmorClassItem_Spell",
    "MonsterLegendaryActionsItem",
    "MonsterLegendaryActionsItemActionsItem",
    "MonsterLegendaryActionsItemActionsItemType",
    "MonsterLegendaryActionsItemAttacksItem",
    "MonsterLegendaryActionsItemDamageItem",
    "MonsterProficienciesItem",
    "MonsterReactionsItem",
    "MonsterReactionsItemActionsItem",
    "MonsterReactionsItemActionsItemType",
    "MonsterReactionsItemAttacksItem",
    "MonsterReactionsItemDamageItem",
    "MonsterSenses",
    "MonsterSize",
    "MonsterSpecialAbilitiesItem",
    "MonsterSpecialAbilitiesItemSpellcasting",
    "MonsterSpecialAbilitiesItemSpellcastingSpellsItem",
    "MonsterSpecialAbilitiesItemUsage",
    "MonsterSpecialAbilitiesItemUsageType",
    "MonsterSpeed",
    "Multiclassing",
    "Option",
    "OptionActionName",
    "OptionActionNameType",
    "OptionAlignments",
    "OptionBonus",
    "OptionChoice",
    "OptionDamage",
    "OptionDamageDice",
    "OptionItem",
    "OptionItems",
    "OptionMinimumScore",
    "OptionOf",
    "OptionSet",
    "OptionSetEquipmentCategory",
    "OptionSetOptionSetType",
    "OptionSetOptionsArray",
    "OptionString",
    "Prerequisite",
    "Proficiency",
    "Race",
    "ResourceDescription",
    "Rule",
    "RuleSection",
    "Skill",
    "Spell",
    "SpellComponentsItem",
    "SpellDamage",
    "SpellPrerequisite",
    "Spellcasting",
    "SpellcastingInfoItem",
    "Subclass",
    "SubclassLevel",
    "SubclassLevelResource",
    "SubclassLevelSpellcasting",
    "SubclassSpellsItem",
    "Subrace",
    "Trait",
    "TraitTraitSpecific",
    "TraitTraitSpecificBreathWeapon",
    "TraitTraitSpecificBreathWeaponBreathWeapon",
    "TraitTraitSpecificBreathWeaponBreathWeaponDamage",
    "TraitTraitSpecificBreathWeaponBreathWeaponUsage",
    "Weapon",
    "WeaponProperty",
    "WeaponRange",
]
