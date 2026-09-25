

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .e_coaching_scores_item_category import ECoachingScoresItemCategory


class ECoachingScoresItem(UniversalBaseModel):
    category: typing.Optional[ECoachingScoresItemCategory] = pydantic.Field(default=None)
    """
    category of the score. Global, ACCELERATION, BREAKING, A/C system, Runing cold engine, Direct Shift Gear, Speed, STT system, ZEV (Zero emission vehicle).
    """

    score: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
