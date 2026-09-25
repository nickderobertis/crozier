

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .predictions_predictions_item_predictions_zero_item_one_value_item_item import (
    PredictionsPredictionsItemPredictionsZeroItemOneValueItemItem,
)


class PredictionsPredictionsItemPredictionsZeroItemOne(UniversalBaseModel):
    label: str
    page: typing.Optional[int] = None
    value: typing.List[typing.List[PredictionsPredictionsItemPredictionsZeroItemOneValueItemItem]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
