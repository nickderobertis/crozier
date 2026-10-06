

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .battle_response_dto_output_statistics import BattleResponseDtoOutputStatistics
from .battle_response_dto_output_warriors_item import BattleResponseDtoOutputWarriorsItem


class BattleResponseDtoOutput(UniversalBaseModel):
    id: str
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    public: bool
    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="userId"), pydantic.Field(alias="userId")]
    account_id: typing_extensions.Annotated[str, FieldMetadata(alias="accountId"), pydantic.Field(alias="accountId")]
    character_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="characterId"), pydantic.Field(alias="characterId")
    ]
    world: str
    duration: float
    type: str
    winner: str
    loser: str
    winning_team: typing_extensions.Annotated[
        float, FieldMetadata(alias="winningTeam"), pydantic.Field(alias="winningTeam")
    ]
    losing_team: typing_extensions.Annotated[
        float, FieldMetadata(alias="losingTeam"), pydantic.Field(alias="losingTeam")
    ]
    honor_points: typing_extensions.Annotated[
        float, FieldMetadata(alias="honorPoints"), pydantic.Field(alias="honorPoints")
    ]
    has_flee: typing_extensions.Annotated[bool, FieldMetadata(alias="hasFlee"), pydantic.Field(alias="hasFlee")]
    matchmaking: bool
    statistics: BattleResponseDtoOutputStatistics
    difficulty_rank: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="difficultyRank"), pydantic.Field(alias="difficultyRank")
    ] = None
    result: typing.Optional[float] = None
    rating_delta: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="ratingDelta"), pydantic.Field(alias="ratingDelta")
    ] = None
    opponent_lvl: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="opponentLvl"), pydantic.Field(alias="opponentLvl")
    ] = None
    opponent_oplvl: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="opponentOplvl"), pydantic.Field(alias="opponentOplvl")
    ] = None
    opponent_rating: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="opponentRating"), pydantic.Field(alias="opponentRating")
    ] = None
    rating: typing.Optional[float] = None
    status: typing.Optional[float] = None
    points_gained: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="pointsGained"), pydantic.Field(alias="pointsGained")
    ] = None
    placement_cur: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="placementCur"), pydantic.Field(alias="placementCur")
    ] = None
    placement_max: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="placementMax"), pydantic.Field(alias="placementMax")
    ] = None
    daily_stage_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="dailyStageId"), pydantic.Field(alias="dailyStageId")
    ] = None
    daily_points_cur: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="dailyPointsCur"), pydantic.Field(alias="dailyPointsCur")
    ] = None
    daily_points_max: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="dailyPointsMax"), pydantic.Field(alias="dailyPointsMax")
    ] = None
    daily_points_step: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="dailyPointsStep"), pydantic.Field(alias="dailyPointsStep")
    ] = None
    daily_rewards_last: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="dailyRewardsLast"), pydantic.Field(alias="dailyRewardsLast")
    ] = None
    daily_rewards_cur: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="dailyRewardsCur"), pydantic.Field(alias="dailyRewardsCur")
    ] = None
    daily_rewards_max: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="dailyRewardsMax"), pydantic.Field(alias="dailyRewardsMax")
    ] = None
    warriors: typing.List[BattleResponseDtoOutputWarriorsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
