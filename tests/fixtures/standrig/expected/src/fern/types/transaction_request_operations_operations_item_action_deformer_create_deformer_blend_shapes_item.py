

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_curve import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemCurve,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_interpolation import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolation,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_kind import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemKind,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_pins_item import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemPinsItem,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_shared_points_item import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemSharedPointsItem,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_transform import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemTransform,
)
from .transaction_request_operations_operations_item_action_deformer_create_deformer_blend_shapes_item_warp import (
    TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemWarp,
)


class TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItem(UniversalBaseModel):
    kind: TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemKind
    transform: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemTransform
    ] = None
    warp: typing.Optional[TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemWarp] = (
        None
    )
    pins: typing.Optional[
        typing.List[TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemPinsItem]
    ] = None
    shared_points: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemSharedPointsItem
            ]
        ],
        FieldMetadata(alias="sharedPoints"),
        pydantic.Field(alias="sharedPoints"),
    ] = None
    id: str
    parameter: str
    neutral_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="neutralInput"), pydantic.Field(alias="neutralInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    interpolation: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemInterpolation
    ] = None
    curve: typing.Optional[
        TransactionRequestOperationsOperationsItemActionDeformerCreateDeformerBlendShapesItemCurve
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
