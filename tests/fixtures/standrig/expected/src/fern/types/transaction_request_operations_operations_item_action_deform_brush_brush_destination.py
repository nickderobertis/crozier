

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_request_operations_operations_item_action_deform_brush_brush_destination_blend_shape_shape import (
    TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShape,
)


class TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_Base(UniversalBaseModel):
    kind: typing.Literal["base"] = "base"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_BlendShape(UniversalBaseModel):
    kind: typing.Literal["blend-shape"] = "blend-shape"
    shape: TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestinationBlendShapeShape

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_Keyform(UniversalBaseModel):
    kind: typing.Literal["keyform"] = "keyform"
    parameter: str
    input: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination = typing_extensions.Annotated[
    typing.Union[
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_Base,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_BlendShape,
        TransactionRequestOperationsOperationsItemActionDeformBrushBrushDestination_Keyform,
    ],
    pydantic.Field(discriminator="kind"),
]
