

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateBattleDtoEventsItemMatchSummaryDailyStage(UniversalBaseModel):
    id: float
    points_cur: float
    points_max: float
    points_step: float
    rewards_last: float
    rewards_cur: float
    rewards_max: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
