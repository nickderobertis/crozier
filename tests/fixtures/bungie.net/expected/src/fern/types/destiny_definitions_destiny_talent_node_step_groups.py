

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyTalentNodeStepGroups(UniversalBaseModel):
    """
    These properties are an attempt to categorize talent node steps by certain common properties. See the related enumerations for the type of properties being categorized.
    """

    damage_types: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="damageTypes")] = None
    guardian_attributes: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="guardianAttributes")
    ] = None
    impact_effects: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="impactEffects")] = None
    light_abilities: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="lightAbilities")] = None
    weapon_performance: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="weaponPerformance")] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
