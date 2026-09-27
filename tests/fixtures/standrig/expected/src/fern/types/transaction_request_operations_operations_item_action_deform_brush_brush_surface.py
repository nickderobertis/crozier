

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_deform_brush_brush_surface_artmesh_space import (
    TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceArtmeshSpace,
)
from .transaction_request_operations_operations_item_action_deform_brush_brush_surface_shared_warp_space import (
    TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceSharedWarpSpace,
)
from .transaction_request_operations_operations_item_action_deform_brush_brush_surface_warp_pins_space import (
    TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceWarpPinsSpace,
)


class TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_Artmesh(UniversalBaseModel):
    kind: typing.Literal["artmesh"] = "artmesh"
    space: TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceArtmeshSpace

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_WarpPins(UniversalBaseModel):
    kind: typing.Literal["warp-pins"] = "warp-pins"
    space: TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceWarpPinsSpace
    width: float
    height: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_SharedWarp(UniversalBaseModel):
    kind: typing.Literal["shared-warp"] = "shared-warp"
    space: TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceSharedWarpSpace

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface = typing_extensions.Annotated[
    typing.Union[
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_Artmesh,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_WarpPins,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface_SharedWarp,
    ],
    pydantic.Field(discriminator="kind"),
]
