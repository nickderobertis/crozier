

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_deform_brush_brush_destination import (
    TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination,
)
from .transaction_request_operations_operations_item_action_deform_brush_brush_effect import (
    TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect,
)
from .transaction_request_operations_operations_item_action_deform_brush_brush_falloff import (
    TransactionRequestOperationsOperationsItemActionDeformBrushBrushFalloff,
)
from .transaction_request_operations_operations_item_action_deform_brush_brush_surface import (
    TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface,
)


class TransactionRequestOperationsOperationsItemActionDeformBrushBrush(UniversalBaseModel):
    surface: TransactionRequestOperationsOperationsItemActionDeformBrushBrushSurface
    center: typing.List[typing.Any]
    radius: float
    effect: TransactionRequestOperationsOperationsItemActionDeformBrushBrushEffect
    iterations: int
    max_displacement: typing_extensions.Annotated[
        float, FieldMetadata(alias="maxDisplacement"), pydantic.Field(alias="maxDisplacement")
    ]
    falloff: TransactionRequestOperationsOperationsItemActionDeformBrushBrushFalloff
    locked_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="lockedIds"), pydantic.Field(alias="lockedIds")
    ] = None
    edges: typing.Optional[typing.List[typing.List[typing.Any]]] = None
    destination: TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
