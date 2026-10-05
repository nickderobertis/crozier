

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BattleResponseDtoOutputWarriorsItem(UniversalBaseModel):
    id: str
    battle_id: typing_extensions.Annotated[str, FieldMetadata(alias="battleId"), pydantic.Field(alias="battleId")]
    original_id: typing_extensions.Annotated[str, FieldMetadata(alias="originalId"), pydantic.Field(alias="originalId")]
    name: str
    lvl: float
    prof: str
    icon: str
    team: float
    turns: float
    turns_lost: typing_extensions.Annotated[float, FieldMetadata(alias="turnsLost"), pydantic.Field(alias="turnsLost")]
    steps: float
    normal_attacks: typing_extensions.Annotated[
        float, FieldMetadata(alias="normalAttacks"), pydantic.Field(alias="normalAttacks")
    ]
    spells_used: typing_extensions.Annotated[
        float, FieldMetadata(alias="spellsUsed"), pydantic.Field(alias="spellsUsed")
    ]
    spells_used_map: typing_extensions.Annotated[
        typing.Dict[str, float], FieldMetadata(alias="spellsUsedMap"), pydantic.Field(alias="spellsUsedMap")
    ]
    is_dead: typing_extensions.Annotated[bool, FieldMetadata(alias="isDead"), pydantic.Field(alias="isDead")]
    surrendered: bool
    fled: bool
    max_hp: typing_extensions.Annotated[float, FieldMetadata(alias="maxHp"), pydantic.Field(alias="maxHp")]
    damage_dealt: typing_extensions.Annotated[
        float, FieldMetadata(alias="damageDealt"), pydantic.Field(alias="damageDealt")
    ]
    distance_damage: typing_extensions.Annotated[
        float, FieldMetadata(alias="distanceDamage"), pydantic.Field(alias="distanceDamage")
    ]
    melee_damage: typing_extensions.Annotated[
        float, FieldMetadata(alias="meleeDamage"), pydantic.Field(alias="meleeDamage")
    ]
    auxiliary_damage: typing_extensions.Annotated[
        float, FieldMetadata(alias="auxiliaryDamage"), pydantic.Field(alias="auxiliaryDamage")
    ]
    fire_damage: typing_extensions.Annotated[
        float, FieldMetadata(alias="fireDamage"), pydantic.Field(alias="fireDamage")
    ]
    frost_damage: typing_extensions.Annotated[
        float, FieldMetadata(alias="frostDamage"), pydantic.Field(alias="frostDamage")
    ]
    lightning_damage: typing_extensions.Annotated[
        float, FieldMetadata(alias="lightningDamage"), pydantic.Field(alias="lightningDamage")
    ]
    third_att_damage: typing_extensions.Annotated[
        float, FieldMetadata(alias="thirdAttDamage"), pydantic.Field(alias="thirdAttDamage")
    ]
    damage_dealt_after_defensive: typing_extensions.Annotated[
        float, FieldMetadata(alias="damageDealtAfterDefensive"), pydantic.Field(alias="damageDealtAfterDefensive")
    ]
    damage_dealt_after_defensive_percentage: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="damageDealtAfterDefensivePercentage"),
        pydantic.Field(alias="damageDealtAfterDefensivePercentage"),
    ]
    damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="damageTaken"), pydantic.Field(alias="damageTaken")
    ]
    distance_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="distanceDamageTaken"), pydantic.Field(alias="distanceDamageTaken")
    ]
    melee_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="meleeDamageTaken"), pydantic.Field(alias="meleeDamageTaken")
    ]
    auxiliary_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="auxiliaryDamageTaken"), pydantic.Field(alias="auxiliaryDamageTaken")
    ]
    fire_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="fireDamageTaken"), pydantic.Field(alias="fireDamageTaken")
    ]
    frost_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="frostDamageTaken"), pydantic.Field(alias="frostDamageTaken")
    ]
    lightning_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="lightningDamageTaken"), pydantic.Field(alias="lightningDamageTaken")
    ]
    third_att_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="thirdAttDamageTaken"), pydantic.Field(alias="thirdAttDamageTaken")
    ]
    flat_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="flatDamageTaken"), pydantic.Field(alias="flatDamageTaken")
    ]
    rage_damage_dealt: typing_extensions.Annotated[
        float, FieldMetadata(alias="rageDamageDealt"), pydantic.Field(alias="rageDamageDealt")
    ]
    true_damage_dealt: typing_extensions.Annotated[
        float, FieldMetadata(alias="trueDamageDealt"), pydantic.Field(alias="trueDamageDealt")
    ]
    true_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="trueDamageTaken"), pydantic.Field(alias="trueDamageTaken")
    ]
    stigma_damage_dealt: typing_extensions.Annotated[
        float, FieldMetadata(alias="stigmaDamageDealt"), pydantic.Field(alias="stigmaDamageDealt")
    ]
    stigma_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="stigmaDamageTaken"), pydantic.Field(alias="stigmaDamageTaken")
    ]
    passive_healing: typing_extensions.Annotated[
        float, FieldMetadata(alias="passiveHealing"), pydantic.Field(alias="passiveHealing")
    ]
    active_healing: typing_extensions.Annotated[
        float, FieldMetadata(alias="activeHealing"), pydantic.Field(alias="activeHealing")
    ]
    armor_pierces: typing_extensions.Annotated[
        float, FieldMetadata(alias="armorPierces"), pydantic.Field(alias="armorPierces")
    ]
    critical_hits: typing_extensions.Annotated[
        float, FieldMetadata(alias="criticalHits"), pydantic.Field(alias="criticalHits")
    ]
    reduced_armor: typing_extensions.Annotated[
        float, FieldMetadata(alias="reducedArmor"), pydantic.Field(alias="reducedArmor")
    ]
    reduced_poison_resistance: typing_extensions.Annotated[
        float, FieldMetadata(alias="reducedPoisonResistance"), pydantic.Field(alias="reducedPoisonResistance")
    ]
    magic_resistance_destroyed: typing_extensions.Annotated[
        float, FieldMetadata(alias="magicResistanceDestroyed"), pydantic.Field(alias="magicResistanceDestroyed")
    ]
    evasions: float
    attacks_evaded: typing_extensions.Annotated[
        float, FieldMetadata(alias="attacksEvaded"), pydantic.Field(alias="attacksEvaded")
    ]
    counters: float
    fast_arrows: typing_extensions.Annotated[
        float, FieldMetadata(alias="fastArrows"), pydantic.Field(alias="fastArrows")
    ]
    blocks: float
    attacks_blocked: typing_extensions.Annotated[
        float, FieldMetadata(alias="attacksBlocked"), pydantic.Field(alias="attacksBlocked")
    ]
    blocked_damage: typing_extensions.Annotated[
        float, FieldMetadata(alias="blockedDamage"), pydantic.Field(alias="blockedDamage")
    ]
    wound_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="woundDamageTaken"), pydantic.Field(alias="woundDamageTaken")
    ]
    poison_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="poisonDamageTaken"), pydantic.Field(alias="poisonDamageTaken")
    ]
    injure_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="injureDamageTaken"), pydantic.Field(alias="injureDamageTaken")
    ]
    injures: float
    crit_wound_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="critWoundDamageTaken"), pydantic.Field(alias="critWoundDamageTaken")
    ]
    fire_passive_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="firePassiveDamageTaken"), pydantic.Field(alias="firePassiveDamageTaken")
    ]
    lightning_passive_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="lightningPassiveDamageTaken"), pydantic.Field(alias="lightningPassiveDamageTaken")
    ]
    destroyed_energy: typing_extensions.Annotated[
        float, FieldMetadata(alias="destroyedEnergy"), pydantic.Field(alias="destroyedEnergy")
    ]
    destroyed_mana: typing_extensions.Annotated[
        float, FieldMetadata(alias="destroyedMana"), pydantic.Field(alias="destroyedMana")
    ]
    regenerated_energy: typing_extensions.Annotated[
        float, FieldMetadata(alias="regeneratedEnergy"), pydantic.Field(alias="regeneratedEnergy")
    ]
    regenerated_mana: typing_extensions.Annotated[
        float, FieldMetadata(alias="regeneratedMana"), pydantic.Field(alias="regeneratedMana")
    ]
    reflected_damage: typing_extensions.Annotated[
        float, FieldMetadata(alias="reflectedDamage"), pydantic.Field(alias="reflectedDamage")
    ]
    reflected_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="reflectedDamageTaken"), pydantic.Field(alias="reflectedDamageTaken")
    ]
    legbons: float
    legbon_curse: typing_extensions.Annotated[
        float, FieldMetadata(alias="legbonCurse"), pydantic.Field(alias="legbonCurse")
    ]
    legbon_cleanse: typing_extensions.Annotated[
        float, FieldMetadata(alias="legbonCleanse"), pydantic.Field(alias="legbonCleanse")
    ]
    legbon_lastheal: typing_extensions.Annotated[
        float, FieldMetadata(alias="legbonLastheal"), pydantic.Field(alias="legbonLastheal")
    ]
    legbon_lastheal_value: typing_extensions.Annotated[
        float, FieldMetadata(alias="legbonLasthealValue"), pydantic.Field(alias="legbonLasthealValue")
    ]
    legbon_glare: typing_extensions.Annotated[
        float, FieldMetadata(alias="legbonGlare"), pydantic.Field(alias="legbonGlare")
    ]
    legbon_holytouch: typing_extensions.Annotated[
        float, FieldMetadata(alias="legbonHolytouch"), pydantic.Field(alias="legbonHolytouch")
    ]
    legbon_holytouch_value: typing_extensions.Annotated[
        float, FieldMetadata(alias="legbonHolytouchValue"), pydantic.Field(alias="legbonHolytouchValue")
    ]
    legbon_critred_value: typing_extensions.Annotated[
        float, FieldMetadata(alias="legbonCritredValue"), pydantic.Field(alias="legbonCritredValue")
    ]
    legbon_facade_value: typing_extensions.Annotated[
        float, FieldMetadata(alias="legbonFacadeValue"), pydantic.Field(alias="legbonFacadeValue")
    ]
    legbon_puncture_value: typing_extensions.Annotated[
        float, FieldMetadata(alias="legbonPunctureValue"), pydantic.Field(alias="legbonPunctureValue")
    ]
    legbon_verycrit: typing_extensions.Annotated[
        float, FieldMetadata(alias="legbonVerycrit"), pydantic.Field(alias="legbonVerycrit")
    ]
    legbon_anguish: typing_extensions.Annotated[
        float, FieldMetadata(alias="legbonAnguish"), pydantic.Field(alias="legbonAnguish")
    ]
    legbon_anguish_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="legbonAnguishDamageTaken"), pydantic.Field(alias="legbonAnguishDamageTaken")
    ]
    ph: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
