

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .player_vs_player_paginated_response_dto_output_battles_item_opponent_warrior import (
    PlayerVsPlayerPaginatedResponseDtoOutputBattlesItemOpponentWarrior,
)
from .player_vs_player_paginated_response_dto_output_battles_item_user_warrior import (
    PlayerVsPlayerPaginatedResponseDtoOutputBattlesItemUserWarrior,
)


class PlayerVsPlayerPaginatedResponseDtoOutputBattlesItem(UniversalBaseModel):
    battle_id: typing_extensions.Annotated[str, FieldMetadata(alias="battleId"), pydantic.Field(alias="battleId")]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    duration: float
    winner: str
    loser: str
    has_flee: typing_extensions.Annotated[bool, FieldMetadata(alias="hasFlee"), pydantic.Field(alias="hasFlee")]
    matchmaking: bool
    rating_delta: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="ratingDelta"), pydantic.Field(alias="ratingDelta")
    ] = None
    user_rating: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="userRating"), pydantic.Field(alias="userRating")
    ] = None
    opponent_rating: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="opponentRating"), pydantic.Field(alias="opponentRating")
    ] = None
    user_warrior: typing_extensions.Annotated[
        PlayerVsPlayerPaginatedResponseDtoOutputBattlesItemUserWarrior,
        FieldMetadata(alias="userWarrior"),
        pydantic.Field(alias="userWarrior"),
    ]
    opponent_warrior: typing_extensions.Annotated[
        PlayerVsPlayerPaginatedResponseDtoOutputBattlesItemOpponentWarrior,
        FieldMetadata(alias="opponentWarrior"),
        pydantic.Field(alias="opponentWarrior"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
