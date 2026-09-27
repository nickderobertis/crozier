

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_curve import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerCurve,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_interpolation import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolation,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_pins_item import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerPinsItem,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_shared_points_item import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerSharedPointsItem,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_transform import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerTransform,
)
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_warp import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerWarp,
)


class TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformer(UniversalBaseModel):
    transform: typing.Optional[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerTransform] = (
        None
    )
    warp: typing.Optional[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerWarp] = None
    pins: typing.Optional[
        typing.List[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerPinsItem]
    ] = None
    shared_points: typing_extensions.Annotated[
        typing.Optional[
            typing.List[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerSharedPointsItem]
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
        TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerInterpolation
    ] = None
    curve: typing.Optional[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
