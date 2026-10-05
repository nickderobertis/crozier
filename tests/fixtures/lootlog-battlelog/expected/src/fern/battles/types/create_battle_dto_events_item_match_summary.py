

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_battle_dto_events_item_match_summary_daily_stage import CreateBattleDtoEventsItemMatchSummaryDailyStage


class CreateBattleDtoEventsItemMatchSummary(UniversalBaseModel):
    difficulty_rank: float
    result: float
    rating_delta: float
    opponent_lvl: float
    opponent_oplvl: float
    opponent_rating: float
    rating: float
    status: float
    placement_cur: typing.Optional[float] = None
    placement_max: typing.Optional[float] = None
    points_gained: typing.Optional[float] = None
    daily_stage: typing.Optional[CreateBattleDtoEventsItemMatchSummaryDailyStage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
