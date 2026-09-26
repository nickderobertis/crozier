

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .predictions_predictions_item_postprocess_config import PredictionsPredictionsItemPostprocessConfig
from .predictions_predictions_item_predictions import PredictionsPredictionsItemPredictions
from .predictions_predictions_item_preprocess_config import PredictionsPredictionsItemPreprocessConfig
from .predictions_predictions_item_status import PredictionsPredictionsItemStatus


class PredictionsPredictionsItem(UniversalBaseModel):
    updated_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedTime"), pydantic.Field(alias="updatedTime")
    ] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    training_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="trainingId"), pydantic.Field(alias="trainingId")
    ] = None
    model_id: typing_extensions.Annotated[str, FieldMetadata(alias="modelId"), pydantic.Field(alias="modelId")]
    next_page: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="nextPage"), pydantic.Field(alias="nextPage")
    ] = None
    postprocess_config: typing_extensions.Annotated[
        typing.Optional[PredictionsPredictionsItemPostprocessConfig],
        FieldMetadata(alias="postprocessConfig"),
        pydantic.Field(alias="postprocessConfig"),
    ] = None
    warnings: typing.Optional[typing.List[str]] = None
    description: typing.Optional[str] = None
    inference_time: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="inferenceTime"), pydantic.Field(alias="inferenceTime")
    ] = None
    error: typing.Optional[str] = None
    agent_run_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="agentRunId"), pydantic.Field(alias="agentRunId")
    ] = None
    predictions: PredictionsPredictionsItemPredictions
    preprocess_config: typing_extensions.Annotated[
        typing.Optional[PredictionsPredictionsItemPreprocessConfig],
        FieldMetadata(alias="preprocessConfig"),
        pydantic.Field(alias="preprocessConfig"),
    ] = None
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    name: typing.Optional[str] = None
    created_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="createdTime"), pydantic.Field(alias="createdTime")
    ]
    document_id: typing_extensions.Annotated[str, FieldMetadata(alias="documentId"), pydantic.Field(alias="documentId")]
    file_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fileUrl"), pydantic.Field(alias="fileUrl")
    ] = None
    prediction_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="predictionId"), pydantic.Field(alias="predictionId")
    ]
    errors: typing.Optional[typing.List[str]] = None
    status: typing.Optional[PredictionsPredictionsItemStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
