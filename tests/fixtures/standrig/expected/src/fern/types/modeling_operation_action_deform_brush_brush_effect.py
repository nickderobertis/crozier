

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ModelingOperationActionDeformBrushBrushEffect_Smooth(UniversalBaseModel):
    mode: typing.Literal["smooth"] = "smooth"
    strength: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationActionDeformBrushBrushEffect_Relax(UniversalBaseModel):
    mode: typing.Literal["relax"] = "relax"
    strength: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationActionDeformBrushBrushEffect_Inflate(UniversalBaseModel):
    mode: typing.Literal["inflate"] = "inflate"
    distance: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationActionDeformBrushBrushEffect_Pinch(UniversalBaseModel):
    mode: typing.Literal["pinch"] = "pinch"
    strength: float
    axis: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationActionDeformBrushBrushEffect_Bend(UniversalBaseModel):
    mode: typing.Literal["bend"] = "bend"
    angle: float
    axis: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelingOperationActionDeformBrushBrushEffect_ContourFollow(UniversalBaseModel):
    mode: typing.Literal["contour-follow"] = "contour-follow"
    strength: float
    guide: typing.List[typing.List[typing.Any]]
    vertex_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="vertexIds"), pydantic.Field(alias="vertexIds")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ModelingOperationActionDeformBrushBrushEffect = typing_extensions.Annotated[
    typing.Union[
        ModelingOperationActionDeformBrushBrushEffect_Smooth,
        ModelingOperationActionDeformBrushBrushEffect_Relax,
        ModelingOperationActionDeformBrushBrushEffect_Inflate,
        ModelingOperationActionDeformBrushBrushEffect_Pinch,
        ModelingOperationActionDeformBrushBrushEffect_Bend,
        ModelingOperationActionDeformBrushBrushEffect_ContourFollow,
    ],
    pydantic.Field(discriminator="mode"),
]
