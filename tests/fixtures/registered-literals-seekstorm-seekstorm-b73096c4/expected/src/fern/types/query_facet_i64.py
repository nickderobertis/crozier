

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_i64i64 import QueryFacetI64I64


class QueryFacetI64(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type i64
    """

    i64: typing_extensions.Annotated[
        QueryFacetI64I64,
        FieldMetadata(alias="I64"),
        pydantic.Field(
            alias="I64", description="Range segment definition for numerical facet field values of type i64"
        ),
    ]
    """
    Range segment definition for numerical facet field values of type i64
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
