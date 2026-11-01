

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .point import Point


class ConvertPointsRequest(UniversalBaseModel):
    from_crs: typing_extensions.Annotated[str, FieldMetadata(alias="fromCRS"), pydantic.Field(alias="fromCRS")]
    points: typing.List[Point]
    to_crs: typing_extensions.Annotated[str, FieldMetadata(alias="toCRS"), pydantic.Field(alias="toCRS")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
