

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_u64u64 import QueryFacetU64U64


class QueryFacetU64(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type u64
    """

    u64: typing_extensions.Annotated[
        QueryFacetU64U64,
        FieldMetadata(alias="U64"),
        pydantic.Field(
            alias="U64", description="Range segment definition for numerical facet field values of type u64"
        ),
    ]
    """
    Range segment definition for numerical facet field values of type u64
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
