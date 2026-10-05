

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PlayerVsPlayerPaginatedResponseDtoOutputBattlesItemUserWarrior(UniversalBaseModel):
    name: str
    lvl: float
    prof: str
    icon: str
    fire_damage: typing_extensions.Annotated[
        float, FieldMetadata(alias="fireDamage"), pydantic.Field(alias="fireDamage")
    ]
    frost_damage: typing_extensions.Annotated[
        float, FieldMetadata(alias="frostDamage"), pydantic.Field(alias="frostDamage")
    ]
    lightning_damage: typing_extensions.Annotated[
        float, FieldMetadata(alias="lightningDamage"), pydantic.Field(alias="lightningDamage")
    ]
    poison_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="poisonDamageTaken"), pydantic.Field(alias="poisonDamageTaken")
    ]
    wound_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="woundDamageTaken"), pydantic.Field(alias="woundDamageTaken")
    ]
    crit_wound_damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="critWoundDamageTaken"), pydantic.Field(alias="critWoundDamageTaken")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
