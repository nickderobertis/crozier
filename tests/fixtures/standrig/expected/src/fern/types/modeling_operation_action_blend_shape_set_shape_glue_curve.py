

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_blend_shape_set_shape_glue_curve_control_points_item import (
    ModelingOperationActionBlendShapeSetShapeGlueCurveControlPointsItem,
)


class ModelingOperationActionBlendShapeSetShapeGlueCurve(UniversalBaseModel):
    control_points: typing_extensions.Annotated[
        typing.List[ModelingOperationActionBlendShapeSetShapeGlueCurveControlPointsItem],
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
