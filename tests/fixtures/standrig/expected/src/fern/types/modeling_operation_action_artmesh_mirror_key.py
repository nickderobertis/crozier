

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_artmesh_mirror_key_curve import ModelingOperationActionArtmeshMirrorKeyCurve
from .modeling_operation_action_artmesh_mirror_key_interpolation import (
    ModelingOperationActionArtmeshMirrorKeyInterpolation,
)


class ModelingOperationActionArtmeshMirrorKey(UniversalBaseModel):
    parameter: str
    source_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="sourceInput"), pydantic.Field(alias="sourceInput")
    ]
    target_input: typing_extensions.Annotated[
        float, FieldMetadata(alias="targetInput"), pydantic.Field(alias="targetInput")
    ]
    axis_u: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="axisU"), pydantic.Field(alias="axisU")
    ] = None
    tolerance: typing.Optional[float] = None
    protect_vertex_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="protectVertexIds"),
        pydantic.Field(alias="protectVertexIds"),
    ] = None
    additive: typing.Optional[bool] = None
    interpolation: typing.Optional[ModelingOperationActionArtmeshMirrorKeyInterpolation] = None
    curve: typing.Optional[ModelingOperationActionArtmeshMirrorKeyCurve] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
