

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tic_recommend_prediction import TicRecommendPrediction


class TicRecommendResponse(UniversalBaseModel):
    predictions: typing.Optional[typing.List[TicRecommendPrediction]] = pydantic.Field(default=None)
    """
    Recommended TIC predictions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
