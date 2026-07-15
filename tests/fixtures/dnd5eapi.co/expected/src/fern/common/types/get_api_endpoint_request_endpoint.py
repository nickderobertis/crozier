

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiEndpointRequestEndpoint(str, enum.Enum):
    ABILITY_SCORES = "ability-scores"
    ALIGNMENTS = "alignments"
    BACKGROUNDS = "backgrounds"
    CLASSES = "classes"
    CONDITIONS = "conditions"
    DAMAGE_TYPES = "damage-types"
    EQUIPMENT = "equipment"
    EQUIPMENT_CATEGORIES = "equipment-categories"
    FEATS = "feats"
    FEATURES = "features"
    LANGUAGES = "languages"
    MAGIC_ITEMS = "magic-items"
    MAGIC_SCHOOLS = "magic-schools"
    MONSTERS = "monsters"
    PROFICIENCIES = "proficiencies"
    RACES = "races"
    RULE_SECTIONS = "rule-sections"
    RULES = "rules"
    SKILLS = "skills"
    SPELLS = "spells"
    SUBCLASSES = "subclasses"
    SUBRACES = "subraces"
    TRAITS = "traits"
    WEAPON_PROPERTIES = "weapon-properties"

    def visit(
        self,
        ability_scores: typing.Callable[[], T_Result],
        alignments: typing.Callable[[], T_Result],
        backgrounds: typing.Callable[[], T_Result],
        classes: typing.Callable[[], T_Result],
        conditions: typing.Callable[[], T_Result],
        damage_types: typing.Callable[[], T_Result],
        equipment: typing.Callable[[], T_Result],
        equipment_categories: typing.Callable[[], T_Result],
        feats: typing.Callable[[], T_Result],
        features: typing.Callable[[], T_Result],
        languages: typing.Callable[[], T_Result],
        magic_items: typing.Callable[[], T_Result],
        magic_schools: typing.Callable[[], T_Result],
        monsters: typing.Callable[[], T_Result],
        proficiencies: typing.Callable[[], T_Result],
        races: typing.Callable[[], T_Result],
        rule_sections: typing.Callable[[], T_Result],
        rules: typing.Callable[[], T_Result],
        skills: typing.Callable[[], T_Result],
        spells: typing.Callable[[], T_Result],
        subclasses: typing.Callable[[], T_Result],
        subraces: typing.Callable[[], T_Result],
        traits: typing.Callable[[], T_Result],
        weapon_properties: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetApiEndpointRequestEndpoint.ABILITY_SCORES:
            return ability_scores()
        if self is GetApiEndpointRequestEndpoint.ALIGNMENTS:
            return alignments()
        if self is GetApiEndpointRequestEndpoint.BACKGROUNDS:
            return backgrounds()
        if self is GetApiEndpointRequestEndpoint.CLASSES:
            return classes()
        if self is GetApiEndpointRequestEndpoint.CONDITIONS:
            return conditions()
        if self is GetApiEndpointRequestEndpoint.DAMAGE_TYPES:
            return damage_types()
        if self is GetApiEndpointRequestEndpoint.EQUIPMENT:
            return equipment()
        if self is GetApiEndpointRequestEndpoint.EQUIPMENT_CATEGORIES:
            return equipment_categories()
        if self is GetApiEndpointRequestEndpoint.FEATS:
            return feats()
        if self is GetApiEndpointRequestEndpoint.FEATURES:
            return features()
        if self is GetApiEndpointRequestEndpoint.LANGUAGES:
            return languages()
        if self is GetApiEndpointRequestEndpoint.MAGIC_ITEMS:
            return magic_items()
        if self is GetApiEndpointRequestEndpoint.MAGIC_SCHOOLS:
            return magic_schools()
        if self is GetApiEndpointRequestEndpoint.MONSTERS:
            return monsters()
        if self is GetApiEndpointRequestEndpoint.PROFICIENCIES:
            return proficiencies()
        if self is GetApiEndpointRequestEndpoint.RACES:
            return races()
        if self is GetApiEndpointRequestEndpoint.RULE_SECTIONS:
            return rule_sections()
        if self is GetApiEndpointRequestEndpoint.RULES:
            return rules()
        if self is GetApiEndpointRequestEndpoint.SKILLS:
            return skills()
        if self is GetApiEndpointRequestEndpoint.SPELLS:
            return spells()
        if self is GetApiEndpointRequestEndpoint.SUBCLASSES:
            return subclasses()
        if self is GetApiEndpointRequestEndpoint.SUBRACES:
            return subraces()
        if self is GetApiEndpointRequestEndpoint.TRAITS:
            return traits()
        if self is GetApiEndpointRequestEndpoint.WEAPON_PROPERTIES:
            return weapon_properties()
