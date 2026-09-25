

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .models_models_item_confidence_version import ModelsModelsItemConfidenceVersion
from .models_models_item_llm_version import ModelsModelsItemLlmVersion
from .models_models_item_postprocess_config import ModelsModelsItemPostprocessConfig
from .models_models_item_preprocess_config import ModelsModelsItemPreprocessConfig
from .models_models_item_status import ModelsModelsItemStatus


class ModelsModelsItem(UniversalBaseModel):
    updated_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedTime"), pydantic.Field(alias="updatedTime")
    ] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    llm_version: typing_extensions.Annotated[
        typing.Optional[ModelsModelsItemLlmVersion],
        FieldMetadata(alias="llmVersion"),
        pydantic.Field(alias="llmVersion"),
    ] = None
    training_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="trainingId"), pydantic.Field(alias="trainingId")
    ] = None
    model_id: typing_extensions.Annotated[str, FieldMetadata(alias="modelId"), pydantic.Field(alias="modelId")]
    postprocess_config: typing_extensions.Annotated[
        typing.Optional[ModelsModelsItemPostprocessConfig],
        FieldMetadata(alias="postprocessConfig"),
        pydantic.Field(alias="postprocessConfig"),
    ] = None
    description: typing.Optional[str] = None
    field_config: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="fieldConfig"),
        pydantic.Field(alias="fieldConfig"),
    ] = None
    version: typing.Optional[int] = None
    organization_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="organizationId"), pydantic.Field(alias="organizationId")
    ]
    confidence_version: typing_extensions.Annotated[
        typing.Optional[ModelsModelsItemConfidenceVersion],
        FieldMetadata(alias="confidenceVersion"),
        pydantic.Field(alias="confidenceVersion"),
    ] = None
    preprocess_config: typing_extensions.Annotated[
        ModelsModelsItemPreprocessConfig,
        FieldMetadata(alias="preprocessConfig"),
        pydantic.Field(alias="preprocessConfig"),
    ]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    updated_field_config_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updatedFieldConfigTime"),
        pydantic.Field(alias="updatedFieldConfigTime"),
    ] = None
    number_of_running_trainings: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfRunningTrainings"), pydantic.Field(alias="numberOfRunningTrainings")
    ]
    name: typing.Optional[str] = None
    number_of_data_bundles: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfDataBundles"), pydantic.Field(alias="numberOfDataBundles")
    ]
    created_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="createdTime"), pydantic.Field(alias="createdTime")
    ]
    statistics: typing.Optional[typing.Dict[str, typing.Any]] = None
    status: ModelsModelsItemStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
