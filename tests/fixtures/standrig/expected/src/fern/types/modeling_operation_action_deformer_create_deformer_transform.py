

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ModelingOperationActionDeformerCreateDeformerTransform(UniversalBaseModel):
    x: float
    y: float
    rotation: float
    scale_x: typing_extensions.Annotated[float, FieldMetadata(alias="scaleX"), pydantic.Field(alias="scaleX")]
    scale_y: typing_extensions.Annotated[float, FieldMetadata(alias="scaleY"), pydantic.Field(alias="scaleY")]
    pivot_x: typing_extensions.Annotated[float, FieldMetadata(alias="pivotX"), pydantic.Field(alias="pivotX")]
    pivot_y: typing_extensions.Annotated[float, FieldMetadata(alias="pivotY"), pydantic.Field(alias="pivotY")]
    opacity: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
