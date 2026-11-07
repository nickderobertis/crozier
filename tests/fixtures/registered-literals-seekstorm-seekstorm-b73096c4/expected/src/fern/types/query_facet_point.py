

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_point_point import QueryFacetPointPoint


class QueryFacetPoint(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type Point (distance between base of type Point and facet field of type Point)
    """

    point: typing_extensions.Annotated[
        QueryFacetPointPoint,
        FieldMetadata(alias="Point"),
        pydantic.Field(
            alias="Point",
            description="Range segment definition for numerical facet field values of type Point (distance between base of type Point and facet field of type Point)",
        ),
    ]
    """
    Range segment definition for numerical facet field values of type Point (distance between base of type Point and facet field of type Point)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
