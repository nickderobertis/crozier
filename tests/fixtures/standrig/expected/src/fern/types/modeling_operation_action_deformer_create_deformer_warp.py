

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_deformer_create_deformer_warp_grid import (
    ModelingOperationActionDeformerCreateDeformerWarpGrid,
)
from .modeling_operation_action_deformer_create_deformer_warp_pin_blend_mode import (
    ModelingOperationActionDeformerCreateDeformerWarpPinBlendMode,
)
from .modeling_operation_action_deformer_create_deformer_warp_pins_item import (
    ModelingOperationActionDeformerCreateDeformerWarpPinsItem,
)


class ModelingOperationActionDeformerCreateDeformerWarp(UniversalBaseModel):
    enabled: bool
    pin_blend_mode: typing_extensions.Annotated[
        typing.Optional[ModelingOperationActionDeformerCreateDeformerWarpPinBlendMode],
        FieldMetadata(alias="pinBlendMode"),
        pydantic.Field(alias="pinBlendMode"),
    ] = None
    bend_x: typing_extensions.Annotated[float, FieldMetadata(alias="bendX"), pydantic.Field(alias="bendX")]
    bend_y: typing_extensions.Annotated[float, FieldMetadata(alias="bendY"), pydantic.Field(alias="bendY")]
    taper_x: typing_extensions.Annotated[float, FieldMetadata(alias="taperX"), pydantic.Field(alias="taperX")]
    taper_y: typing_extensions.Annotated[float, FieldMetadata(alias="taperY"), pydantic.Field(alias="taperY")]
    grid: ModelingOperationActionDeformerCreateDeformerWarpGrid
    pins: typing.Optional[typing.List[ModelingOperationActionDeformerCreateDeformerWarpPinsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
