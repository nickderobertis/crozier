

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_i32i32 import QueryFacetI32I32


class QueryFacetI32(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type i32
    """

    i32: typing_extensions.Annotated[
        QueryFacetI32I32,
        FieldMetadata(alias="I32"),
        pydantic.Field(
            alias="I32", description="Range segment definition for numerical facet field values of type i32"
        ),
    ]
    """
    Range segment definition for numerical facet field values of type i32
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
