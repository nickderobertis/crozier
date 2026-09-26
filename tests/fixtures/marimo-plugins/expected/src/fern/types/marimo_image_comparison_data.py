

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .marimo_image_comparison_data_direction import MarimoImageComparisonDataDirection


class MarimoImageComparisonData(UniversalBaseModel):
    before_src: typing_extensions.Annotated[str, FieldMetadata(alias="beforeSrc"), pydantic.Field(alias="beforeSrc")]
    after_src: typing_extensions.Annotated[str, FieldMetadata(alias="afterSrc"), pydantic.Field(alias="afterSrc")]
    value: typing.Optional[float] = None
    direction: typing.Optional[MarimoImageComparisonDataDirection] = None
    width: typing.Optional[str] = None
    height: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
