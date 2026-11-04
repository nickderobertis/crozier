

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .game_get_by_id_response_game import GameGetByIdResponseGame
from .game_get_by_id_response_reviews_item import GameGetByIdResponseReviewsItem
from .game_get_by_id_response_stats import GameGetByIdResponseStats


class GameGetByIdResponse(UniversalBaseModel):
    game: GameGetByIdResponseGame
    reviews: typing.List[GameGetByIdResponseReviewsItem]
    stats: typing.Optional[GameGetByIdResponseStats] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
