

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_deformer_rotation_metadata_metadata_angle_range import (
    ModelingOperationActionDeformerRotationMetadataMetadataAngleRange,
)
from .modeling_operation_action_deformer_rotation_metadata_metadata_angle_unit import (
    ModelingOperationActionDeformerRotationMetadataMetadataAngleUnit,
)
from .modeling_operation_action_deformer_rotation_metadata_metadata_parent_composition import (
    ModelingOperationActionDeformerRotationMetadataMetadataParentComposition,
)
from .modeling_operation_action_deformer_rotation_metadata_metadata_pivot import (
    ModelingOperationActionDeformerRotationMetadataMetadataPivot,
)
from .modeling_operation_action_deformer_rotation_metadata_metadata_pivot_space import (
    ModelingOperationActionDeformerRotationMetadataMetadataPivotSpace,
)
from .modeling_operation_action_deformer_rotation_metadata_metadata_shape_preservation import (
    ModelingOperationActionDeformerRotationMetadataMetadataShapePreservation,
)


class ModelingOperationActionDeformerRotationMetadataMetadata(UniversalBaseModel):
    version: float
    angle_range: typing_extensions.Annotated[
        ModelingOperationActionDeformerRotationMetadataMetadataAngleRange,
        FieldMetadata(alias="angleRange"),
        pydantic.Field(alias="angleRange"),
    ]
    angle_unit: typing_extensions.Annotated[
        ModelingOperationActionDeformerRotationMetadataMetadataAngleUnit,
        FieldMetadata(alias="angleUnit"),
        pydantic.Field(alias="angleUnit"),
    ]
    pivot: ModelingOperationActionDeformerRotationMetadataMetadataPivot
    pivot_space: typing_extensions.Annotated[
        ModelingOperationActionDeformerRotationMetadataMetadataPivotSpace,
        FieldMetadata(alias="pivotSpace"),
        pydantic.Field(alias="pivotSpace"),
    ]
    shape_preservation: typing_extensions.Annotated[
        ModelingOperationActionDeformerRotationMetadataMetadataShapePreservation,
        FieldMetadata(alias="shapePreservation"),
        pydantic.Field(alias="shapePreservation"),
    ]
    parent_composition: typing_extensions.Annotated[
        ModelingOperationActionDeformerRotationMetadataMetadataParentComposition,
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
