

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AnnotationsFileLabelsRulersValue(UniversalBaseModel):
    color: typing.Optional[str] = None
    stroke_width: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ] = None
    fill_color: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fillColor"), pydantic.Field(alias="fillColor")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
