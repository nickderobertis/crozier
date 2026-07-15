

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiRuleSectionsIndexRequestIndex(str, enum.Enum):
    ABILITY_CHECKS = "ability-checks"
    ABILITY_SCORES_AND_MODIFIERS = "ability-scores-and-modifiers"
    ACTIONS_IN_COMBAT = "actions-in-combat"
    ADVANTAGE_AND_DISADVANTAGE = "advantage-and-disadvantage"
    BETWEEN_ADVENTURES = "between-adventures"
    CASTING_A_SPELL = "casting-a-spell"
    COVER = "cover"
    DAMAGE_AND_HEALING = "damage-and-healing"
    DISEASES = "diseases"
    FANTASY_HISTORICAL_PANTHEONS = "fantasy-historical-pantheons"
    MADNESS = "madness"
    MAKING_AN_ATTACK = "making-an-attack"
    MOUNTED_COMBAT = "mounted-combat"
    MOVEMENT = "movement"
    MOVEMENT_AND_POSITION = "movement-and-position"
    OBJECTS = "objects"
    POISONS = "poisons"
    PROFICIENCY_BONUS = "proficiency-bonus"
    RESTING = "resting"
    SAVING_THROWS = "saving-throws"
    SENTIENT_MAGIC_ITEMS = "sentient-magic-items"
    STANDARD_EXCHANGE_RATES = "standard-exchange-rates"
    THE_ENVIRONMENT = "the-environment"
    THE_ORDER_OF_COMBAT = "the-order-of-combat"
    THE_PLANES_OF_EXISTENCE = "the-planes-of-existence"
    TIME = "time"
    TRAPS = "traps"
    UNDERWATER_COMBAT = "underwater-combat"
    USING_EACH_ABILITY = "using-each-ability"
    WHAT_IS_A_SPELL = "what-is-a-spell"

    def visit(
        self,
        ability_checks: typing.Callable[[], T_Result],
        ability_scores_and_modifiers: typing.Callable[[], T_Result],
        actions_in_combat: typing.Callable[[], T_Result],
        advantage_and_disadvantage: typing.Callable[[], T_Result],
        between_adventures: typing.Callable[[], T_Result],
        casting_a_spell: typing.Callable[[], T_Result],
        cover: typing.Callable[[], T_Result],
        damage_and_healing: typing.Callable[[], T_Result],
        diseases: typing.Callable[[], T_Result],
        fantasy_historical_pantheons: typing.Callable[[], T_Result],
        madness: typing.Callable[[], T_Result],
        making_an_attack: typing.Callable[[], T_Result],
        mounted_combat: typing.Callable[[], T_Result],
        movement: typing.Callable[[], T_Result],
        movement_and_position: typing.Callable[[], T_Result],
        objects: typing.Callable[[], T_Result],
        poisons: typing.Callable[[], T_Result],
        proficiency_bonus: typing.Callable[[], T_Result],
        resting: typing.Callable[[], T_Result],
        saving_throws: typing.Callable[[], T_Result],
        sentient_magic_items: typing.Callable[[], T_Result],
        standard_exchange_rates: typing.Callable[[], T_Result],
        the_environment: typing.Callable[[], T_Result],
        the_order_of_combat: typing.Callable[[], T_Result],
        the_planes_of_existence: typing.Callable[[], T_Result],
        time: typing.Callable[[], T_Result],
        traps: typing.Callable[[], T_Result],
        underwater_combat: typing.Callable[[], T_Result],
        using_each_ability: typing.Callable[[], T_Result],
        what_is_a_spell: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiRuleSectionsIndexRequestIndex.ABILITY_CHECKS:
            return ability_checks()
        if self is GetApiRuleSectionsIndexRequestIndex.ABILITY_SCORES_AND_MODIFIERS:
            return ability_scores_and_modifiers()
        if self is GetApiRuleSectionsIndexRequestIndex.ACTIONS_IN_COMBAT:
            return actions_in_combat()
        if self is GetApiRuleSectionsIndexRequestIndex.ADVANTAGE_AND_DISADVANTAGE:
            return advantage_and_disadvantage()
        if self is GetApiRuleSectionsIndexRequestIndex.BETWEEN_ADVENTURES:
            return between_adventures()
        if self is GetApiRuleSectionsIndexRequestIndex.CASTING_A_SPELL:
            return casting_a_spell()
        if self is GetApiRuleSectionsIndexRequestIndex.COVER:
            return cover()
        if self is GetApiRuleSectionsIndexRequestIndex.DAMAGE_AND_HEALING:
            return damage_and_healing()
        if self is GetApiRuleSectionsIndexRequestIndex.DISEASES:
            return diseases()
        if self is GetApiRuleSectionsIndexRequestIndex.FANTASY_HISTORICAL_PANTHEONS:
            return fantasy_historical_pantheons()
        if self is GetApiRuleSectionsIndexRequestIndex.MADNESS:
            return madness()
        if self is GetApiRuleSectionsIndexRequestIndex.MAKING_AN_ATTACK:
            return making_an_attack()
        if self is GetApiRuleSectionsIndexRequestIndex.MOUNTED_COMBAT:
            return mounted_combat()
        if self is GetApiRuleSectionsIndexRequestIndex.MOVEMENT:
            return movement()
        if self is GetApiRuleSectionsIndexRequestIndex.MOVEMENT_AND_POSITION:
            return movement_and_position()
        if self is GetApiRuleSectionsIndexRequestIndex.OBJECTS:
            return objects()
        if self is GetApiRuleSectionsIndexRequestIndex.POISONS:
            return poisons()
        if self is GetApiRuleSectionsIndexRequestIndex.PROFICIENCY_BONUS:
            return proficiency_bonus()
        if self is GetApiRuleSectionsIndexRequestIndex.RESTING:
            return resting()
        if self is GetApiRuleSectionsIndexRequestIndex.SAVING_THROWS:
            return saving_throws()
        if self is GetApiRuleSectionsIndexRequestIndex.SENTIENT_MAGIC_ITEMS:
            return sentient_magic_items()
        if self is GetApiRuleSectionsIndexRequestIndex.STANDARD_EXCHANGE_RATES:
            return standard_exchange_rates()
        if self is GetApiRuleSectionsIndexRequestIndex.THE_ENVIRONMENT:
            return the_environment()
        if self is GetApiRuleSectionsIndexRequestIndex.THE_ORDER_OF_COMBAT:
            return the_order_of_combat()
        if self is GetApiRuleSectionsIndexRequestIndex.THE_PLANES_OF_EXISTENCE:
            return the_planes_of_existence()
        if self is GetApiRuleSectionsIndexRequestIndex.TIME:
            return time()
        if self is GetApiRuleSectionsIndexRequestIndex.TRAPS:
            return traps()
        if self is GetApiRuleSectionsIndexRequestIndex.UNDERWATER_COMBAT:
            return underwater_combat()
        if self is GetApiRuleSectionsIndexRequestIndex.USING_EACH_ABILITY:
            return using_each_ability()
        if self is GetApiRuleSectionsIndexRequestIndex.WHAT_IS_A_SPELL:
            return what_is_a_spell()
