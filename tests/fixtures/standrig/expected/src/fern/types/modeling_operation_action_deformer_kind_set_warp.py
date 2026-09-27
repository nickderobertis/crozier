

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_deformer_kind_set_warp_grid import ModelingOperationActionDeformerKindSetWarpGrid
from .modeling_operation_action_deformer_kind_set_warp_pin_blend_mode import (
    ModelingOperationActionDeformerKindSetWarpPinBlendMode,
)
from .modeling_operation_action_deformer_kind_set_warp_pins_item import (
    ModelingOperationActionDeformerKindSetWarpPinsItem,
)


class ModelingOperationActionDeformerKindSetWarp(UniversalBaseModel):
    enabled: bool
    pin_blend_mode: typing_extensions.Annotated[
        typing.Optional[ModelingOperationActionDeformerKindSetWarpPinBlendMode],
        FieldMetadata(alias="pinBlendMode"),
        pydantic.Field(alias="pinBlendMode"),
    ] = None
    bend_x: typing_extensions.Annotated[float, FieldMetadata(alias="bendX"), pydantic.Field(alias="bendX")]
    bend_y: typing_extensions.Annotated[float, FieldMetadata(alias="bendY"), pydantic.Field(alias="bendY")]
    taper_x: typing_extensions.Annotated[float, FieldMetadata(alias="taperX"), pydantic.Field(alias="taperX")]
    taper_y: typing_extensions.Annotated[float, FieldMetadata(alias="taperY"), pydantic.Field(alias="taperY")]
    grid: ModelingOperationActionDeformerKindSetWarpGrid
    pins: typing.Optional[typing.List[ModelingOperationActionDeformerKindSetWarpPinsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
