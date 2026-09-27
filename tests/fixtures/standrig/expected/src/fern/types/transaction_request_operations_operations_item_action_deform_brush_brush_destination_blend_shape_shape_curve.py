

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape_curve_control_points_item import (
    TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeCurveControlPointsItem,
)


class TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeCurve(
    UniversalBaseModel
):
    control_points: typing_extensions.Annotated[
        typing.List[
            TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShapeCurveControlPointsItem
        ],
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
