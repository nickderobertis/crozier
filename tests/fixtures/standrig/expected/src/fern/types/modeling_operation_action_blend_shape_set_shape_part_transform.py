

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ModelingOperationActionBlendShapeSetShapePartTransform(UniversalBaseModel):
    x: typing.Optional[float] = None
    y: typing.Optional[float] = None
    rotation: typing.Optional[float] = None
    scale_x: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="scaleX"), pydantic.Field(alias="scaleX")
    ] = None
    scale_y: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="scaleY"), pydantic.Field(alias="scaleY")
    ] = None
    opacity: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
