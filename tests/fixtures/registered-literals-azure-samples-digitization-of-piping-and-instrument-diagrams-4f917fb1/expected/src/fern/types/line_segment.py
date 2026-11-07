

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LineSegment(UniversalBaseModel):
    """
    This class represents the line segment detected on a P&ID image.
    """

    start_x: typing_extensions.Annotated[float, FieldMetadata(alias="startX"), pydantic.Field(alias="startX")]
    start_y: typing_extensions.Annotated[float, FieldMetadata(alias="startY"), pydantic.Field(alias="startY")]
    end_x: typing_extensions.Annotated[float, FieldMetadata(alias="endX"), pydantic.Field(alias="endX")]
    end_y: typing_extensions.Annotated[float, FieldMetadata(alias="endY"), pydantic.Field(alias="endY")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
