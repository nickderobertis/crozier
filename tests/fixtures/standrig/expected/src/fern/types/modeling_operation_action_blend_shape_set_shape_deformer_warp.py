

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ModelingOperationActionBlendShapeSetShapeDeformerWarp(UniversalBaseModel):
    bend_x: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="bendX"), pydantic.Field(alias="bendX")
    ] = None
    bend_y: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="bendY"), pydantic.Field(alias="bendY")
    ] = None
    taper_x: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="taperX"), pydantic.Field(alias="taperX")
    ] = None
    taper_y: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="taperY"), pydantic.Field(alias="taperY")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
