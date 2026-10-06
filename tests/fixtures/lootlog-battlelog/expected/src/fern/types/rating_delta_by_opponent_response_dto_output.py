

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RatingDeltaByOpponentResponseDtoOutput(UniversalBaseModel):
    opponent_id: typing_extensions.Annotated[str, FieldMetadata(alias="opponentId"), pydantic.Field(alias="opponentId")]
    opponent_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="opponentName"), pydantic.Field(alias="opponentName")
    ]
    opponent_icon: typing_extensions.Annotated[
        str, FieldMetadata(alias="opponentIcon"), pydantic.Field(alias="opponentIcon")
    ]
    opponent_prof: typing_extensions.Annotated[
        str, FieldMetadata(alias="opponentProf"), pydantic.Field(alias="opponentProf")
    ]
    opponent_lvl: typing_extensions.Annotated[
        float, FieldMetadata(alias="opponentLvl"), pydantic.Field(alias="opponentLvl")
    ]
    total_rating_delta: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalRatingDelta"), pydantic.Field(alias="totalRatingDelta")
    ]
    wins: float
    losses: float
    total_battles: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalBattles"), pydantic.Field(alias="totalBattles")
    ]
    avg_rating_delta: typing_extensions.Annotated[
        float, FieldMetadata(alias="avgRatingDelta"), pydantic.Field(alias="avgRatingDelta")
    ]
    last_battle_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastBattleDate"), pydantic.Field(alias="lastBattleDate")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
