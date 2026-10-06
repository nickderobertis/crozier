

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .player_vs_player_paginated_response_dto_output_battles_item import (
    PlayerVsPlayerPaginatedResponseDtoOutputBattlesItem,
)
from .player_vs_player_paginated_response_dto_output_meta import PlayerVsPlayerPaginatedResponseDtoOutputMeta
from .player_vs_player_paginated_response_dto_output_pagination import (
    PlayerVsPlayerPaginatedResponseDtoOutputPagination,
)


class PlayerVsPlayerPaginatedResponseDtoOutput(UniversalBaseModel):
    battles: typing.List[PlayerVsPlayerPaginatedResponseDtoOutputBattlesItem]
    pagination: PlayerVsPlayerPaginatedResponseDtoOutputPagination
    meta: PlayerVsPlayerPaginatedResponseDtoOutputMeta

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
