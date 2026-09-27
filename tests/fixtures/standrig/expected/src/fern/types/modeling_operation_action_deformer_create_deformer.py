

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_deformer_create_deformer_bindings_item import (
    ModelingOperationActionDeformerCreateDeformerBindingsItem,
)
from .modeling_operation_action_deformer_create_deformer_blend_shapes_item import (
    ModelingOperationActionDeformerCreateDeformerBlendShapesItem,
)
from .modeling_operation_action_deformer_create_deformer_kind import ModelingOperationActionDeformerCreateDeformerKind
from .modeling_operation_action_deformer_create_deformer_multi_bindings_item import (
    ModelingOperationActionDeformerCreateDeformerMultiBindingsItem,
)
from .modeling_operation_action_deformer_create_deformer_origin import (
    ModelingOperationActionDeformerCreateDeformerOrigin,
)
from .modeling_operation_action_deformer_create_deformer_rotation_metadata import (
    ModelingOperationActionDeformerCreateDeformerRotationMetadata,
)
from .modeling_operation_action_deformer_create_deformer_shared_warp import (
    ModelingOperationActionDeformerCreateDeformerSharedWarp,
)
from .modeling_operation_action_deformer_create_deformer_transform import (
    ModelingOperationActionDeformerCreateDeformerTransform,
)
from .modeling_operation_action_deformer_create_deformer_warp import ModelingOperationActionDeformerCreateDeformerWarp


class ModelingOperationActionDeformerCreateDeformer(UniversalBaseModel):
    blend_shapes: typing_extensions.Annotated[
        typing.Optional[typing.List[ModelingOperationActionDeformerCreateDeformerBlendShapesItem]],
        FieldMetadata(alias="blendShapes"),
        pydantic.Field(alias="blendShapes"),
    ] = None
    id: str
    name: str
    kind: ModelingOperationActionDeformerCreateDeformerKind
    parent_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId")
    ] = None
    visible: bool
    locked: typing.Optional[bool] = None
    origin: ModelingOperationActionDeformerCreateDeformerOrigin
    transform: ModelingOperationActionDeformerCreateDeformerTransform
    warp: typing.Optional[ModelingOperationActionDeformerCreateDeformerWarp] = None
    bindings: typing.Optional[typing.List[ModelingOperationActionDeformerCreateDeformerBindingsItem]] = None
    shared_warp: typing_extensions.Annotated[
        typing.Optional[ModelingOperationActionDeformerCreateDeformerSharedWarp],
        FieldMetadata(alias="sharedWarp"),
        pydantic.Field(alias="sharedWarp"),
    ] = None
    target_part_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="targetPartIds"), pydantic.Field(alias="targetPartIds")
    ] = None
    multi_bindings: typing_extensions.Annotated[
        typing.Optional[typing.List[ModelingOperationActionDeformerCreateDeformerMultiBindingsItem]],
        FieldMetadata(alias="multiBindings"),
        pydantic.Field(alias="multiBindings"),
    ] = None
    tags: typing.Optional[typing.List[str]] = None
    rotation_metadata: typing_extensions.Annotated[
        typing.Optional[ModelingOperationActionDeformerCreateDeformerRotationMetadata],
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
