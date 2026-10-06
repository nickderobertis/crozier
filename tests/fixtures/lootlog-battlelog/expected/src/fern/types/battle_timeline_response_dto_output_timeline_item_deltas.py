

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .battle_timeline_response_dto_output_timeline_item_deltas_by_warrior_value import (
    BattleTimelineResponseDtoOutputTimelineItemDeltasByWarriorValue,
)


class BattleTimelineResponseDtoOutputTimelineItemDeltas(UniversalBaseModel):
    damage: float
    healing: float
    mitigation: float
    resource_pressure: typing_extensions.Annotated[
        float, FieldMetadata(alias="resourcePressure"), pydantic.Field(alias="resourcePressure")
    ]
    energy_pressure: typing_extensions.Annotated[
        float, FieldMetadata(alias="energyPressure"), pydantic.Field(alias="energyPressure")
    ]
    mana_pressure: typing_extensions.Annotated[
        float, FieldMetadata(alias="manaPressure"), pydantic.Field(alias="manaPressure")
    ]
    by_warrior: typing_extensions.Annotated[
        typing.Dict[str, BattleTimelineResponseDtoOutputTimelineItemDeltasByWarriorValue],
        FieldMetadata(alias="byWarrior"),
        pydantic.Field(alias="byWarrior"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
