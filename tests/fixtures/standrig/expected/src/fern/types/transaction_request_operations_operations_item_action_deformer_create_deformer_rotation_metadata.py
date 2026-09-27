

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_angle_range import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataAngleRange,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_angle_unit import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataAngleUnit,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_parent_composition import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataParentComposition,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_pivot import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivot,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_pivot_space import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivotSpace,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata_shape_preservation import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservation,
)


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadata(UniversalBaseModel):
    version: float
    angle_range: typing_extensions.Annotated[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataAngleRange,
        FieldMetadata(alias="angleRange"),
        pydantic.Field(alias="angleRange"),
    ]
    angle_unit: typing_extensions.Annotated[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataAngleUnit,
        FieldMetadata(alias="angleUnit"),
        pydantic.Field(alias="angleUnit"),
    ]
    pivot: TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivot
    pivot_space: typing_extensions.Annotated[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataPivotSpace,
        FieldMetadata(alias="pivotSpace"),
        pydantic.Field(alias="pivotSpace"),
    ]
    shape_preservation: typing_extensions.Annotated[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataShapePreservation,
        FieldMetadata(alias="shapePreservation"),
        pydantic.Field(alias="shapePreservation"),
    ]
    parent_composition: typing_extensions.Annotated[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadataParentComposition,
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
