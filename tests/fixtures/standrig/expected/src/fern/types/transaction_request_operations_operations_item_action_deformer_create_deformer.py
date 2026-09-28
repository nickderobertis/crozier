

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_deformer_create_deformer_bindings_item import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItem,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItem,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_kind import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKind,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_multi_bindings_item import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItem,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_origin import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerOrigin,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_rotation_metadata import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadata,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_shared_warp import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarp,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_transform import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerTransform,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_warp import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarp,
)


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformer(UniversalBaseModel):
    blend_shapes: typing_extensions.Annotated[
        typing.Optional[
            typing.List[TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItem]
        ],
        FieldMetadata(alias="blendShapes"),
        pydantic.Field(alias="blendShapes"),
    ] = None
    id: str
    name: str
    kind: TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerKind
    parent_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId")
    ] = None
    visible: bool
    locked: typing.Optional[bool] = None
    origin: TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerOrigin
    transform: TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerTransform
    warp: typing.Optional[TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerWarp] = None
    bindings: typing.Optional[
        typing.List[TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBindingsItem]
    ] = None
    shared_warp: typing_extensions.Annotated[
        typing.Optional[TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerSharedWarp],
        FieldMetadata(alias="sharedWarp"),
        pydantic.Field(alias="sharedWarp"),
    ] = None
    target_part_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="targetPartIds"), pydantic.Field(alias="targetPartIds")
    ] = None
    multi_bindings: typing_extensions.Annotated[
        typing.Optional[
            typing.List[TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerMultiBindingsItem]
        ],
        FieldMetadata(alias="multiBindings"),
        pydantic.Field(alias="multiBindings"),
    ] = None
    tags: typing.Optional[typing.List[str]] = None
    rotation_metadata: typing_extensions.Annotated[
        typing.Optional[TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerRotationMetadata],
        FieldMetadata(alias="rotationMetadata"),
        pydantic.Field(alias="rotationMetadata"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
