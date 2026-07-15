

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from .api_reference import ApiReference
from .monster_actions_item import MonsterActionsItem
from .monster_alignments import MonsterAlignments
from .monster_armor_class_item import MonsterArmorClassItem
from .monster_legendary_actions_item import MonsterLegendaryActionsItem
from .monster_proficiencies_item import MonsterProficienciesItem
from .monster_reactions_item import MonsterReactionsItem
from .monster_senses import MonsterSenses
from .monster_size import MonsterSize
from .monster_special_abilities_item import MonsterSpecialAbilitiesItem
from .monster_speed import MonsterSpeed
from .resource_description import ResourceDescription


class Monster(ApiReference, ResourceDescription):
    """
    `Monster`
    """

    charisma: typing.Optional[float] = pydantic.Field(default=None)
    """
    A monster's ability to charm or intimidate a player.
    """

    constitution: typing.Optional[float] = pydantic.Field(default=None)
    """
    How sturdy a monster is."
    """

    dexterity: typing.Optional[float] = pydantic.Field(default=None)
    """
    The monster's ability for swift movement or stealth
    """

    intelligence: typing.Optional[float] = pydantic.Field(default=None)
    """
    The monster's ability to outsmart a player.
    """

    strength: typing.Optional[float] = pydantic.Field(default=None)
    """
    How hard a monster can hit a player.
    """

    wisdom: typing.Optional[float] = pydantic.Field(default=None)
    """
    A monster's ability to ascertain the player's plan.
    """

    actions: typing.Optional[typing.List[MonsterActionsItem]] = pydantic.Field(default=None)
    """
    A list of actions that are available to the monster to take during combat.
    """

    alignments: typing.Optional[MonsterAlignments] = pydantic.Field(default=None)
    """
    A creature's general moral and personal attitudes.
    """

    armor_class: typing.Optional[typing.List[MonsterArmorClassItem]] = pydantic.Field(default=None)
    """
    The difficulty for a player to successfully deal damage to a monster.
    """

    challenge_rating: typing.Optional[float] = pydantic.Field(default=None)
    """
    A monster's challenge rating is a guideline number that says when a monster becomes an appropriate challenge against the party's average level. For example. A group of 4 players with an average level of 4 would have an appropriate combat challenge against a monster with a challenge rating of 4 but a monster with a challenge rating of 8 against the same group of players would pose a significant threat.
    """

    condition_immunities: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    A list of conditions that a monster is immune to.
    """

    damage_immunities: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of damage types that a monster will take double damage from.
    """

    damage_resistances: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of damage types that a monster will take half damage from.
    """

    damage_vulnerabilities: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of damage types that a monster will take double damage from.
    """

    forms: typing.Optional[typing.List[ApiReference]] = pydantic.Field(default=None)
    """
    List of other related monster entries that are of the same form. Only applicable to Lycanthropes that have multiple forms.
    """

    hit_dice: typing.Optional[str] = pydantic.Field(default=None)
    """
    The hit die of a monster can be used to make a version of the same monster whose hit points are determined by the roll of the die. For example: A monster with 2d6 would have its hit points determine by rolling a 6 sided die twice.
    """

    hit_points: typing.Optional[float] = pydantic.Field(default=None)
    """
    The hit points of a monster determine how much damage it is able to take before it can be defeated.
    """

    hit_points_roll: typing.Optional[str] = pydantic.Field(default=None)
    """
    The roll for determining a monster's hit points, which consists of the hit dice (e.g. 18d10) and the modifier determined by its Constitution (e.g. +36). For example, 18d10+36
    """

    image: typing.Optional[str] = pydantic.Field(default=None)
    """
    The image url of the monster.
    """

    languages: typing.Optional[str] = pydantic.Field(default=None)
    """
    The languages a monster is able to speak.
    """

    legendary_actions: typing.Optional[typing.List[MonsterLegendaryActionsItem]] = pydantic.Field(default=None)
    """
    A list of legendary actions that are available to the monster to take during combat.
    """

    proficiencies: typing.Optional[typing.List[MonsterProficienciesItem]] = pydantic.Field(default=None)
    """
    A list of proficiencies of a monster.
    """

    reactions: typing.Optional[typing.List[MonsterReactionsItem]] = pydantic.Field(default=None)
    """
    A list of reactions that is available to the monster to take during combat.
    """

    senses: typing.Optional[MonsterSenses] = pydantic.Field(default=None)
    """
    Monsters typically have a passive perception but they might also have other senses to detect players.
    """

    size: typing.Optional[MonsterSize] = pydantic.Field(default=None)
    """
    The size of the monster ranging from Tiny to Gargantuan."
    """

    special_abilities: typing.Optional[typing.List[MonsterSpecialAbilitiesItem]] = pydantic.Field(default=None)
    """
    A list of the monster's special abilities.
    """

    speed: typing.Optional[MonsterSpeed] = pydantic.Field(default=None)
    """
    Speed for a monster determines how fast it can move per turn.
    """

    subtype: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub-category of a monster used for classification of monsters."
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of monster.
    """

    xp: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of experience points (XP) a monster is worth is based on its challenge rating.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Monster)
