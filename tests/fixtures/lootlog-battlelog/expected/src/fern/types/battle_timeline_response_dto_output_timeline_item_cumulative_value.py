

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BattleTimelineResponseDtoOutputTimelineItemCumulativeValue(UniversalBaseModel):
    damage_dealt: typing_extensions.Annotated[
        float, FieldMetadata(alias="damageDealt"), pydantic.Field(alias="damageDealt")
    ]
    damage_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="damageTaken"), pydantic.Field(alias="damageTaken")
    ]
    healing_done: typing_extensions.Annotated[
        float, FieldMetadata(alias="healingDone"), pydantic.Field(alias="healingDone")
    ]
    healing_received: typing_extensions.Annotated[
        float, FieldMetadata(alias="healingReceived"), pydantic.Field(alias="healingReceived")
    ]
    mitigation: float
    resource_delta: typing_extensions.Annotated[
        float, FieldMetadata(alias="resourceDelta"), pydantic.Field(alias="resourceDelta")
    ]
    resource_pressure: typing_extensions.Annotated[
        float, FieldMetadata(alias="resourcePressure"), pydantic.Field(alias="resourcePressure")
    ]
    energy_pressure: typing_extensions.Annotated[
        float, FieldMetadata(alias="energyPressure"), pydantic.Field(alias="energyPressure")
    ]
    mana_pressure: typing_extensions.Annotated[
        float, FieldMetadata(alias="manaPressure"), pydantic.Field(alias="manaPressure")
    ]
    absorb_gained: typing_extensions.Annotated[
        float, FieldMetadata(alias="absorbGained"), pydantic.Field(alias="absorbGained")
    ]
    absorb_spent: typing_extensions.Annotated[
        float, FieldMetadata(alias="absorbSpent"), pydantic.Field(alias="absorbSpent")
    ]
    magic_absorb_gained: typing_extensions.Annotated[
        float, FieldMetadata(alias="magicAbsorbGained"), pydantic.Field(alias="magicAbsorbGained")
    ]
    magic_absorb_spent: typing_extensions.Annotated[
        float, FieldMetadata(alias="magicAbsorbSpent"), pydantic.Field(alias="magicAbsorbSpent")
    ]
    control_applied: typing_extensions.Annotated[
        float, FieldMetadata(alias="controlApplied"), pydantic.Field(alias="controlApplied")
    ]
    control_taken: typing_extensions.Annotated[
        float, FieldMetadata(alias="controlTaken"), pydantic.Field(alias="controlTaken")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
