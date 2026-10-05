

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .head_to_head_paginated_response_dto_output_records_item_last_battle_opponent_warrior import (
    HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleOpponentWarrior,
)
from .head_to_head_paginated_response_dto_output_records_item_last_battle_result import (
    HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleResult,
)
from .head_to_head_paginated_response_dto_output_records_item_last_battle_user_warrior import (
    HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleUserWarrior,
)


class HeadToHeadPaginatedResponseDtoOutputRecordsItem(UniversalBaseModel):
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
    last_battle_result: typing_extensions.Annotated[
        HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleResult,
        FieldMetadata(alias="lastBattleResult"),
        pydantic.Field(alias="lastBattleResult"),
    ]
    last_battle_user_warrior: typing_extensions.Annotated[
        HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleUserWarrior,
        FieldMetadata(alias="lastBattleUserWarrior"),
        pydantic.Field(alias="lastBattleUserWarrior"),
    ]
    last_battle_opponent_warrior: typing_extensions.Annotated[
        HeadToHeadPaginatedResponseDtoOutputRecordsItemLastBattleOpponentWarrior,
        FieldMetadata(alias="lastBattleOpponentWarrior"),
        pydantic.Field(alias="lastBattleOpponentWarrior"),
    ]
    wins: float
    losses: float
    total_battles: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalBattles"), pydantic.Field(alias="totalBattles")
    ]
    win_rate: typing_extensions.Annotated[float, FieldMetadata(alias="winRate"), pydantic.Field(alias="winRate")]
    last_battle_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastBattleDate"), pydantic.Field(alias="lastBattleDate")
    ]
    total_rating_delta: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="totalRatingDelta"), pydantic.Field(alias="totalRatingDelta")
    ] = None
    avg_rating_delta: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="avgRatingDelta"), pydantic.Field(alias="avgRatingDelta")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
