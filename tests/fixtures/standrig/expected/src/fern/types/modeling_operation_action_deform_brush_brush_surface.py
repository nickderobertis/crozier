

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_deform_brush_brush_surface_artmesh_space import (
    ModelingOperationActionDeformBrushBrushSurfaceArtmeshSpace,
)
from .modeling_operation_action_deform_brush_brush_surface_shared_warp_space import (
    ModelingOperationActionDeformBrushBrushSurfaceSharedWarpSpace,
)
from .modeling_operation_action_deform_brush_brush_surface_warp_pins_space import (
    ModelingOperationActionDeformBrushBrushSurfaceWarpPinsSpace,
)


class ModelingOperationActionDeformBrushBrushSurface_Artmesh(UniversalBaseModel):
    kind: typing.Literal["artmesh"] = "artmesh"
    space: ModelingOperationActionDeformBrushBrushSurfaceArtmeshSpace

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationActionDeformBrushBrushSurface_WarpPins(UniversalBaseModel):
    kind: typing.Literal["warp-pins"] = "warp-pins"
    space: ModelingOperationActionDeformBrushBrushSurfaceWarpPinsSpace
    width: float
    height: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationActionDeformBrushBrushSurface_SharedWarp(UniversalBaseModel):
    kind: typing.Literal["shared-warp"] = "shared-warp"
    space: ModelingOperationActionDeformBrushBrushSurfaceSharedWarpSpace

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ModelingOperationActionDeformBrushBrushSurface = typing_extensions.Annotated[
    typing.Union[
        ModelingOperationActionDeformBrushBrushSurface_Artmesh,
        ModelingOperationActionDeformBrushBrushSurface_WarpPins,
        ModelingOperationActionDeformBrushBrushSurface_SharedWarp,
    ],
    pydantic.Field(discriminator="kind"),
]
