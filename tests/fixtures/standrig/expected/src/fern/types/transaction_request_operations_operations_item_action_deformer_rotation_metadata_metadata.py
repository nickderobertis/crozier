

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_angle_range import (
    TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataAngleRange,
)
from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_angle_unit import (
    TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataAngleUnit,
)
from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_parent_composition import (
    TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentComposition,
)
from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_pivot import (
    TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivot,
)
from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_pivot_space import (
    TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivotSpace,
)
from .transaction_request_operations_operations_item_action_deformer_rotation_metadata_metadata_shape_preservation import (
    TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservation,
)


class TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadata(UniversalBaseModel):
    version: float
    angle_range: typing_extensions.Annotated[
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataAngleRange,
        FieldMetadata(alias="angleRange"),
        pydantic.Field(alias="angleRange"),
    ]
    angle_unit: typing_extensions.Annotated[
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataAngleUnit,
        FieldMetadata(alias="angleUnit"),
        pydantic.Field(alias="angleUnit"),
    ]
    pivot: TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivot
    pivot_space: typing_extensions.Annotated[
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataPivotSpace,
        FieldMetadata(alias="pivotSpace"),
        pydantic.Field(alias="pivotSpace"),
    ]
    shape_preservation: typing_extensions.Annotated[
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataShapePreservation,
        FieldMetadata(alias="shapePreservation"),
        pydantic.Field(alias="shapePreservation"),
    ]
    parent_composition: typing_extensions.Annotated[
        TransactionRequestOperationsOperationsItemActionDeformerRotationMetadataMetadataParentComposition,
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
