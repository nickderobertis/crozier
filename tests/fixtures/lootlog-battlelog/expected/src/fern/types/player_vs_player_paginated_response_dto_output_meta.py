

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .player_vs_player_paginated_response_dto_output_meta_performance import (
    PlayerVsPlayerPaginatedResponseDtoOutputMetaPerformance,
)


class PlayerVsPlayerPaginatedResponseDtoOutputMeta(UniversalBaseModel):
    performance: PlayerVsPlayerPaginatedResponseDtoOutputMetaPerformance

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
