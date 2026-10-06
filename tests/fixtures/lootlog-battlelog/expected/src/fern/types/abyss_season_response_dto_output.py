

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AbyssSeasonResponseDtoOutput(UniversalBaseModel):
    id: str
    started_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ]
    ended_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="endedAt"), pydantic.Field(alias="endedAt")]
    total_battles: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalBattles"), pydantic.Field(alias="totalBattles")
    ]
    wins: float
    losses: float
    win_rate: typing_extensions.Annotated[float, FieldMetadata(alias="winRate"), pydantic.Field(alias="winRate")]
    total_rating_delta: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalRatingDelta"), pydantic.Field(alias="totalRatingDelta")
    ]
    peak_rating: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="peakRating"), pydantic.Field(alias="peakRating")
    ] = None
    total_points_gained: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="totalPointsGained"), pydantic.Field(alias="totalPointsGained")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
