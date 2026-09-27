

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ModelingOperationActionArtmeshQualityQuality(UniversalBaseModel):
    min_triangle_area: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="minTriangleArea"), pydantic.Field(alias="minTriangleArea")
    ] = None
    max_triangle_aspect_ratio: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="maxTriangleAspectRatio"),
        pydantic.Field(alias="maxTriangleAspectRatio"),
    ] = None
    boundary_vertex_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="boundaryVertexIds"),
        pydantic.Field(alias="boundaryVertexIds"),
    ] = None
    locked_vertex_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="lockedVertexIds"),
        pydantic.Field(alias="lockedVertexIds"),
    ] = None
    pinned_vertex_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="pinnedVertexIds"),
        pydantic.Field(alias="pinnedVertexIds"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
