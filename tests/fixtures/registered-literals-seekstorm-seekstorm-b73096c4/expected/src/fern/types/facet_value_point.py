

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .vec import Vec


class FacetValuePoint(UniversalBaseModel):
    """
    Point value: latitude/lat, longitude/lon
    """

    point: typing_extensions.Annotated[
        Vec,
        FieldMetadata(alias="Point"),
        pydantic.Field(alias="Point", description="Point value: latitude/lat, longitude/lon"),
    ]
    """
    Point value: latitude/lat, longitude/lon
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
