

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_blend_shape_set_shape_deformer_curve_control_points_item import (
    TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerCurveControlPointsItem,
)


class TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerCurve(UniversalBaseModel):
    control_points: typing_extensions.Annotated[
        typing.List[TransactionRequestOperationsOperationsItemActionBlendShapeSetShapeDeformerCurveControlPointsItem],
        FieldMetadata(alias="controlPoints"),
        pydantic.Field(alias="controlPoints"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
