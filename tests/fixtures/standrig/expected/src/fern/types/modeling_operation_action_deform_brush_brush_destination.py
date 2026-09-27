

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modeling_operation_action_deform_brush_brush_destination_blend_shape_shape import (
    ModelingOperationActionDeformBrushBrushDestinationBlendShapeShape,
)


class ModelingOperationActionDeformBrushBrushDestination_Base(UniversalBaseModel):
    kind: typing.Literal["base"] = "base"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationActionDeformBrushBrushDestination_BlendShape(UniversalBaseModel):
    kind: typing.Literal["blend-shape"] = "blend-shape"
    shape: ModelingOperationActionDeformBrushBrushDestinationBlendShapeShape

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationActionDeformBrushBrushDestination_Keyform(UniversalBaseModel):
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


ModelingOperationActionDeformBrushBrushDestination = typing_extensions.Annotated[
    typing.Union[
        ModelingOperationActionDeformBrushBrushDestination_Base,
        ModelingOperationActionDeformBrushBrushDestination_BlendShape,
        ModelingOperationActionDeformBrushBrushDestination_Keyform,
    ],
    pydantic.Field(discriminator="kind"),
]
