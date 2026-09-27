

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_deformer_transform_operator import ModelingOperationActionDeformerTransformOperator
from .modeling_operation_action_deformer_transform_property import ModelingOperationActionDeformerTransformProperty


class ModelingOperationActionDeformerTransform(UniversalBaseModel):
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    property: ModelingOperationActionDeformerTransformProperty
    operator: ModelingOperationActionDeformerTransformOperator
    value: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
