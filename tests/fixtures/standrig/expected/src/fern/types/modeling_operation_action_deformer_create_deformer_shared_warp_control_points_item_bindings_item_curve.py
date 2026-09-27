

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item_curve_control_points_item import (
    ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurveControlPointsItem,
)


class ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurve(UniversalBaseModel):
    control_points: typing_extensions.Annotated[
        typing.List[
            ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItemCurveControlPointsItem
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
