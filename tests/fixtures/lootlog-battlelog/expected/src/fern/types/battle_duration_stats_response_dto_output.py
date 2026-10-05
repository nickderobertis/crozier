

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .battle_duration_stats_response_dto_output_fastest import BattleDurationStatsResponseDtoOutputFastest
from .battle_duration_stats_response_dto_output_longest import BattleDurationStatsResponseDtoOutputLongest


class BattleDurationStatsResponseDtoOutput(UniversalBaseModel):
    avg_win_duration: typing_extensions.Annotated[
        float, FieldMetadata(alias="avgWinDuration"), pydantic.Field(alias="avgWinDuration")
    ]
    avg_loss_duration: typing_extensions.Annotated[
        float, FieldMetadata(alias="avgLossDuration"), pydantic.Field(alias="avgLossDuration")
    ]
    fastest: typing.Optional[BattleDurationStatsResponseDtoOutputFastest] = None
    longest: typing.Optional[BattleDurationStatsResponseDtoOutputLongest] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
