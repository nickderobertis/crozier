

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CombatProfileResponseDtoOutputSummary(UniversalBaseModel):
    total_battles: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalBattles"), pydantic.Field(alias="totalBattles")
    ]
    wins: float
    losses: float
    win_rate: typing_extensions.Annotated[float, FieldMetadata(alias="winRate"), pydantic.Field(alias="winRate")]
    total_ph: typing_extensions.Annotated[float, FieldMetadata(alias="totalPH"), pydantic.Field(alias="totalPH")]
    total_rating_delta: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalRatingDelta"), pydantic.Field(alias="totalRatingDelta")
    ]
    avg_turns: typing_extensions.Annotated[float, FieldMetadata(alias="avgTurns"), pydantic.Field(alias="avgTurns")]
    avg_duration: typing_extensions.Annotated[
        float, FieldMetadata(alias="avgDuration"), pydantic.Field(alias="avgDuration")
    ]
    damage_per_turn: typing_extensions.Annotated[
        float, FieldMetadata(alias="damagePerTurn"), pydantic.Field(alias="damagePerTurn")
    ]
    mitigation_rate: typing_extensions.Annotated[
        float, FieldMetadata(alias="mitigationRate"), pydantic.Field(alias="mitigationRate")
    ]
    control_rate: typing_extensions.Annotated[
        float, FieldMetadata(alias="controlRate"), pydantic.Field(alias="controlRate")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
