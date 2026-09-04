

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AnnotationsFileToolsPolygonsItemFrameOfReference(UniversalBaseModel):
    plane_normal: typing_extensions.Annotated[
        typing.List[typing.Any], FieldMetadata(alias="planeNormal"), pydantic.Field(alias="planeNormal")
    ]
    plane_origin: typing_extensions.Annotated[
        typing.List[typing.Any], FieldMetadata(alias="planeOrigin"), pydantic.Field(alias="planeOrigin")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
