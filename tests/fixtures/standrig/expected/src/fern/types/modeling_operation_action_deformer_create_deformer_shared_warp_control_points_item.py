

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_deformer_create_deformer_shared_warp_control_points_item_bindings_item import (
    ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItem,
)


class ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItem(UniversalBaseModel):
    bindings: typing.Optional[
        typing.List[ModelingOperationActionDeformerCreateDeformerSharedWarpControlPointsItemBindingsItem]
    ] = None
    id: str
    column: float
    row: float
    offset_x: typing_extensions.Annotated[float, FieldMetadata(alias="offsetX"), pydantic.Field(alias="offsetX")]
    offset_y: typing_extensions.Annotated[float, FieldMetadata(alias="offsetY"), pydantic.Field(alias="offsetY")]
    enabled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
