

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_deform_brush_brush_surface_warp_pins_space import (
    TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceWarpPinsSpace,
)


class TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurfaceWarpPins(UniversalBaseModel):
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
