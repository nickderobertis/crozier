

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Shape(UniversalBaseModel):
    """
    A geometric shape.
    """

    shape_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="shapeType"), pydantic.Field(alias="shapeType", description="Discriminator value.")
    ]
    """
    Discriminator value.
    """

    area: typing.Optional[float] = pydantic.Field(default=None)
    """
    Area in square units.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
