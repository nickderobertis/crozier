

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_point_point import FacetFilterPointPoint


class FacetFilterPoint(UniversalBaseModel):
    """
    Point proximity range filter
    """

    point: typing_extensions.Annotated[
        FacetFilterPointPoint,
        FieldMetadata(alias="Point"),
        pydantic.Field(alias="Point", description="Point proximity range filter"),
    ]
    """
    Point proximity range filter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
