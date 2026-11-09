

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .categorical_score import CategoricalScore
from .get_scores_response_trace_data import GetScoresResponseTraceData


class GetScoresResponseDataCategorical(CategoricalScore):
    trace: GetScoresResponseTraceData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
