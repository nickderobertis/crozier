

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .predictions_order import PredictionsOrder
from .predictions_predictions_item import PredictionsPredictionsItem
from .predictions_sort_by import PredictionsSortBy


class Predictions(UniversalBaseModel):
    model_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="modelId"), pydantic.Field(alias="modelId")
    ] = None
    next_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextToken"), pydantic.Field(alias="nextToken")
    ] = None
    sort_by: typing_extensions.Annotated[
        typing.Optional[PredictionsSortBy], FieldMetadata(alias="sortBy"), pydantic.Field(alias="sortBy")
    ] = None
    predictions: typing.List[PredictionsPredictionsItem]
    order: typing.Optional[PredictionsOrder] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
