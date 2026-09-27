

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ModelingOperationActionDeformBrushBrushEffectContourFollow(UniversalBaseModel):
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
