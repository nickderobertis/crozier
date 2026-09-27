

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_deformer_create_deformer_rotation_metadata_angle_range import (
    ModelingOperationActionDeformerCreateDeformerRotationMetadataAngleRange,
)
from .modeling_operation_action_deformer_create_deformer_rotation_metadata_angle_unit import (
    ModelingOperationActionDeformerCreateDeformerRotationMetadataAngleUnit,
)
from .modeling_operation_action_deformer_create_deformer_rotation_metadata_parent_composition import (
    ModelingOperationActionDeformerCreateDeformerRotationMetadataParentComposition,
)
from .modeling_operation_action_deformer_create_deformer_rotation_metadata_pivot import (
    ModelingOperationActionDeformerCreateDeformerRotationMetadataPivot,
)
from .modeling_operation_action_deformer_create_deformer_rotation_metadata_pivot_space import (
    ModelingOperationActionDeformerCreateDeformerRotationMetadataPivotSpace,
)
from .modeling_operation_action_deformer_create_deformer_rotation_metadata_shape_preservation import (
    ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservation,
)


class ModelingOperationActionDeformerCreateDeformerRotationMetadata(UniversalBaseModel):
    version: float
    angle_range: typing_extensions.Annotated[
        ModelingOperationActionDeformerCreateDeformerRotationMetadataAngleRange,
        FieldMetadata(alias="angleRange"),
        pydantic.Field(alias="angleRange"),
    ]
    angle_unit: typing_extensions.Annotated[
        ModelingOperationActionDeformerCreateDeformerRotationMetadataAngleUnit,
        FieldMetadata(alias="angleUnit"),
        pydantic.Field(alias="angleUnit"),
    ]
    pivot: ModelingOperationActionDeformerCreateDeformerRotationMetadataPivot
    pivot_space: typing_extensions.Annotated[
        ModelingOperationActionDeformerCreateDeformerRotationMetadataPivotSpace,
        FieldMetadata(alias="pivotSpace"),
        pydantic.Field(alias="pivotSpace"),
    ]
    shape_preservation: typing_extensions.Annotated[
        ModelingOperationActionDeformerCreateDeformerRotationMetadataShapePreservation,
        FieldMetadata(alias="shapePreservation"),
        pydantic.Field(alias="shapePreservation"),
    ]
    parent_composition: typing_extensions.Annotated[
        ModelingOperationActionDeformerCreateDeformerRotationMetadataParentComposition,
        FieldMetadata(alias="parentComposition"),
        pydantic.Field(alias="parentComposition"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
