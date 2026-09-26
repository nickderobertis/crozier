

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .predictions_predictions_item_predictions_zero_item_one_value_item_item_source import (
    PredictionsPredictionsItemPredictionsZeroItemOneValueItemItemSource,
)


class PredictionsPredictionsItemPredictionsZeroItemOneValueItemItem(UniversalBaseModel):
    validators: typing.Optional[typing.List[typing.Any]] = None
    confidence: float
    warnings: typing.Optional[typing.List[str]] = None
    rotation: typing.Optional[int] = None
    label: str
    source: typing.Optional[PredictionsPredictionsItemPredictionsZeroItemOneValueItemItemSource] = None
    formatters: typing.Optional[typing.List[typing.Any]] = None
    raw_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="rawValue"), pydantic.Field(alias="rawValue")
    ] = None
    attention_map: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[float]]],
        FieldMetadata(alias="attentionMap"),
        pydantic.Field(alias="attentionMap"),
    ] = None
    location: typing.Optional[typing.List[float]] = None
    page: typing.Optional[int] = None
    value: typing.Optional[str] = None
    errors: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
