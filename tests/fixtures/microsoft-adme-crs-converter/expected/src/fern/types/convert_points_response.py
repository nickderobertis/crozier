

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .point import Point


class ConvertPointsResponse(UniversalBaseModel):
    operations_applied: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="operationsApplied"),
        pydantic.Field(alias="operationsApplied"),
    ] = None
    points: typing.Optional[typing.List[Point]] = None
    success_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="successCount"), pydantic.Field(alias="successCount")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
