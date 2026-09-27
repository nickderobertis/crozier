

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_artmesh_blend_shape_curve import ModelingOperationActionArtmeshBlendShapeCurve
from .modeling_operation_action_artmesh_blend_shape_interpolation import (
    ModelingOperationActionArtmeshBlendShapeInterpolation,
)
from .modeling_operation_action_artmesh_blend_shape_offsets_item import (
    ModelingOperationActionArtmeshBlendShapeOffsetsItem,
)


class ModelingOperationActionArtmeshBlendShape(UniversalBaseModel):
    id: str
    parameter: str
    neutral_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="neutralInput"), pydantic.Field(alias="neutralInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    offsets: typing.List[ModelingOperationActionArtmeshBlendShapeOffsetsItem]
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionArtmeshBlendShapeInterpolation] = None
    curve: typing.Optional[ModelingOperationActionArtmeshBlendShapeCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
