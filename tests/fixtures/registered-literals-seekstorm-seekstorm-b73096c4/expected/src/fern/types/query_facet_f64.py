

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_f64f64 import QueryFacetF64F64


class QueryFacetF64(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type f64
    """

    f64: typing_extensions.Annotated[
        QueryFacetF64F64,
        FieldMetadata(alias="F64"),
        pydantic.Field(
            alias="F64", description="Range segment definition for numerical facet field values of type f64"
        ),
    ]
    """
    Range segment definition for numerical facet field values of type f64
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
